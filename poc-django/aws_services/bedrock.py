"""
AWS Bedrock service for AI responses
"""
import boto3
import json
import logging
from django.conf import settings

logger = logging.getLogger(__name__)


class BedrockService:
    """AWS Bedrock integration"""
    
    def __init__(self):
        self.client = boto3.client('bedrock-runtime', region_name=settings.AWS_DEFAULT_REGION)
        self.model_id = settings.BEDROCK_MODEL_ID
    
    def generate_response(self, query, context=""):
        """Generate AI response"""
        try:
            system_prompt = """You are AI Krishi Mitra, an agricultural advisor for Indian farmers.
Provide practical, actionable advice in simple language.
Focus on crop management, pest control, weather-based recommendations, and organic practices.
Keep responses concise and farmer-friendly."""

            user_prompt = f"""Context: {context}

Farmer's Question: {query}

Provide helpful agricultural advice:"""

            request_body = {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 500,
                "temperature": 0.7,
                "messages": [{"role": "user", "content": user_prompt}],
                "system": system_prompt
            }
            
            response = self.client.invoke_model(
                modelId=self.model_id,
                body=json.dumps(request_body)
            )
            
            response_body = json.loads(response['body'].read())
            
            if 'content' in response_body and len(response_body['content']) > 0:
                return response_body['content'][0]['text']
            
            return "I'm having trouble generating a response. Please try again."
            
        except Exception as e:
            logger.error(f"Bedrock error: {str(e)}")
            return "I'm currently unavailable. Please try again later."
