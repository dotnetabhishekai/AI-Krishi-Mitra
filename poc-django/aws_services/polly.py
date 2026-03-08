"""
AWS Polly service for text-to-speech
"""
import boto3
import logging
from django.conf import settings

logger = logging.getLogger(__name__)


class PollyService:
    """AWS Polly integration"""
    
    def __init__(self):
        self.client = boto3.client('polly', region_name=settings.AWS_DEFAULT_REGION)
        self.s3_client = boto3.client('s3', region_name=settings.AWS_DEFAULT_REGION)
    
    def synthesize(self, text, language='hi'):
        """Convert text to speech"""
        try:
            import uuid
            
            # Map language to voice
            voice_map = {
                'hi': 'Aditi',
                'en': 'Raveena',
                'te': 'Aditi',
                'ta': 'Aditi',
                'mr': 'Aditi'
            }
            voice_id = voice_map.get(language, 'Aditi')
            
            # Synthesize speech
            response = self.client.synthesize_speech(
                Text=text,
                OutputFormat='mp3',
                VoiceId=voice_id,
                Engine='neural'
            )
            
            # Upload to S3
            audio_data = response['AudioStream'].read()
            
            bucket = settings.AWS_S3_BUCKET
            key = f"audio/responses/{uuid.uuid4()}.mp3"
            
            self.s3_client.put_object(
                Bucket=bucket,
                Key=key,
                Body=audio_data,
                ContentType='audio/mpeg'
            )
            
            # Generate pre-signed URL
            url = self.s3_client.generate_presigned_url(
                'get_object',
                Params={'Bucket': bucket, 'Key': key},
                ExpiresIn=3600
            )
            
            logger.info(f"Speech synthesized: {key}")
            return url
            
        except Exception as e:
            logger.error(f"Polly error: {str(e)}")
            return None
