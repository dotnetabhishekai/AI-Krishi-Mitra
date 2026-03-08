"""WebSocket consumer for real-time AWS Transcribe streaming."""
import asyncio
import json
import logging
from urllib.parse import parse_qs

from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings
from amazon_transcribe.client import TranscribeStreamingClient
from amazon_transcribe.handlers import TranscriptResultStreamHandler

logger = logging.getLogger(__name__)

LANGUAGE_MAP = {
    'en': 'en-IN',
    'hi': 'hi-IN',
    'te': 'te-IN',
    'ta': 'ta-IN',
    'mr': 'mr-IN',
    'kn': 'kn-IN',
    'bn': 'bn-IN',
    'gu': 'gu-IN',
}


def _has_placeholder_aws_credentials() -> bool:
    """Detect default placeholder credentials from local .env setup."""
    access_key = (settings.AWS_ACCESS_KEY_ID or '').strip()
    secret_key = (settings.AWS_SECRET_ACCESS_KEY or '').strip()

    placeholder_tokens = {
        '',
        'your-aws-access-key',
        'your-aws-secret-key',
    }

    return access_key in placeholder_tokens or secret_key in placeholder_tokens


class _TranscriptEventHandler(TranscriptResultStreamHandler):
    """Push completed transcript chunks to the browser over websocket."""

    def __init__(self, stream, websocket):
        super().__init__(stream)
        self.websocket = websocket

    async def handle_transcript_event(self, transcript_event):
        for result in transcript_event.transcript.results:
            if not result.alternatives:
                continue

            await self.websocket.send(text_data=json.dumps({
                'text': result.alternatives[0].transcript,
                'is_partial': result.is_partial,
            }))


class TranscribeConsumer(AsyncWebsocketConsumer):
    """Stream mic PCM chunks from browser to AWS Transcribe in real time."""

    async def connect(self):
        await self.accept()

        self.stream = None
        self.handler_task = None

        try:
            if _has_placeholder_aws_credentials():
                await self.send(text_data=json.dumps({
                    'error': 'AWS credentials are not configured. Update AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY in poc-django/.env and restart the server.'
                }))
                await self.close(code=4001)
                return

            query_string = parse_qs(self.scope.get('query_string', b'').decode())
            language = query_string.get('lang', ['en'])[0].strip().lower()
            language_code = LANGUAGE_MAP.get(language, 'en-IN')

            client = TranscribeStreamingClient(
                region=settings.AWS_DEFAULT_REGION or 'ap-south-1'
            )

            self.stream = await client.start_stream_transcription(
                language_code=language_code,
                media_sample_rate_hz=16000,
                media_encoding='pcm',
            )

            handler = _TranscriptEventHandler(self.stream.output_stream, self)
            self.handler_task = asyncio.create_task(handler.handle_events())
        except Exception as exc:
            logger.exception('Failed to initialize transcribe stream: %s', exc)

            error_text = str(exc)
            if 'UnrecognizedClientException' in error_text or 'security token' in error_text.lower():
                client_error = 'AWS credentials are invalid. Please update AWS keys/session token and restart server.'
            else:
                client_error = 'Unable to start voice transcription stream.'

            await self.send(text_data=json.dumps({
                'error': client_error
            }))
            await self.close(code=4002)

    async def receive(self, text_data=None, bytes_data=None):
        if not self.stream or not bytes_data:
            return

        try:
            await self.stream.input_stream.send_audio_event(audio_chunk=bytes_data)
        except Exception as exc:
            logger.exception('Error streaming audio chunk: %s', exc)

    async def disconnect(self, close_code):
        if self.stream:
            try:
                await self.stream.input_stream.end_stream()
            except Exception:
                pass

        if self.handler_task:
            self.handler_task.cancel()
