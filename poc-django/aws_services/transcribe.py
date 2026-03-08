"""
AWS Transcribe service for voice-to-text
"""
import boto3
import time
import logging
from django.conf import settings

logger = logging.getLogger(__name__)


class TranscribeService:
    """AWS Transcribe integration"""
    
    def __init__(self):
        self.client = boto3.client('transcribe', region_name=settings.AWS_DEFAULT_REGION)
    
    def transcribe(self, audio_url, language='hi-IN'):
        """Transcribe audio to text"""
        try:
            import uuid
            
            job_name = f"transcribe-{uuid.uuid4()}"
            
            # Map language codes
            lang_map = {
                'en': 'en-IN',
                'hi': 'hi-IN',
                'te': 'te-IN',
                'ta': 'ta-IN',
                'mr': 'mr-IN'
            }
            language_code = lang_map.get(language, 'hi-IN')
            
            # Start transcription job
            self.client.start_transcription_job(
                TranscriptionJobName=job_name,
                Media={'MediaFileUri': audio_url},
                MediaFormat='ogg',
                LanguageCode=language_code
            )
            
            # Wait for completion
            max_wait = 60
            wait_time = 0
            
            while wait_time < max_wait:
                status = self.client.get_transcription_job(
                    TranscriptionJobName=job_name
                )
                
                job_status = status['TranscriptionJob']['TranscriptionJobStatus']
                
                if job_status == 'COMPLETED':
                    transcript_uri = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
                    
                    # Download transcript
                    import requests
                    response = requests.get(transcript_uri, timeout=10)
                    transcript_data = response.json()
                    
                    text = transcript_data['results']['transcripts'][0]['transcript']
                    logger.info(f"Transcription completed: {text[:50]}...")
                    return text
                
                elif job_status == 'FAILED':
                    logger.error("Transcription job failed")
                    return None
                
                time.sleep(2)
                wait_time += 2
            
            logger.warning("Transcription timeout")
            return None
            
        except Exception as e:
            logger.error(f"Transcribe error: {str(e)}")
            return None
