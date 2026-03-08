"""
AWS S3 service for file storage
"""
import boto3
import json
import logging
from django.conf import settings
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


class S3Service:
    """AWS S3 integration"""
    
    def __init__(self):
        self.client = boto3.client('s3', region_name=settings.AWS_DEFAULT_REGION)
        self.bucket = settings.AWS_S3_BUCKET
    
    def upload_audio(self, audio_file, phone_number):
        """Upload audio file to S3"""
        try:
            import uuid
            from datetime import datetime
            
            timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
            unique_id = str(uuid.uuid4())[:8]
            key = f"audio/{phone_number}/{timestamp}_{unique_id}.ogg"
            
            self.client.upload_fileobj(
                audio_file,
                self.bucket,
                key,
                ExtraArgs={'ContentType': 'audio/ogg'}
            )
            
            url = f"s3://{self.bucket}/{key}"
            logger.info(f"Uploaded audio to {url}")
            return url
            
        except ClientError as e:
            logger.error(f"S3 upload error: {str(e)}")
            raise
    
    def upload_image(self, image_file, phone_number):
        """Upload image file to S3"""
        try:
            import uuid
            from datetime import datetime
            
            timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
            unique_id = str(uuid.uuid4())[:8]
            key = f"images/{phone_number}/{timestamp}_{unique_id}.jpg"
            
            self.client.upload_fileobj(
                image_file,
                self.bucket,
                key,
                ExtraArgs={'ContentType': 'image/jpeg'}
            )
            
            url = f"s3://{self.bucket}/{key}"
            logger.info(f"Uploaded image to {url}")
            return url
            
        except ClientError as e:
            logger.error(f"S3 upload error: {str(e)}")
            raise
    
    def get_knowledge_base(self):
        """Load knowledge base from S3"""
        try:
            response = self.client.get_object(
                Bucket=self.bucket,
                Key='knowledge/agricultural_knowledge.json'
            )
            
            content = response['Body'].read()
            knowledge = json.loads(content)
            return knowledge
            
        except ClientError as e:
            logger.warning(f"Knowledge base not found in S3: {str(e)}")
            # Return default knowledge
            return self._get_default_knowledge()
    
    def _get_default_knowledge(self):
        """Default knowledge base"""
        return {
            "crops": {
                "rice": {
                    "name": "Rice",
                    "scientific_name": "Oryza sativa",
                    "season": "Kharif (June-November)",
                    "water": "High (flooded fields)",
                    "soil": "Clay loam, well-drained",
                    "pests": ["Stem borer", "Leaf folder", "Brown plant hopper"],
                    "diseases": ["Blast", "Bacterial leaf blight", "Sheath blight"]
                },
                "wheat": {
                    "name": "Wheat",
                    "scientific_name": "Triticum aestivum",
                    "season": "Rabi (November-April)",
                    "water": "Moderate",
                    "soil": "Loamy, well-drained",
                    "pests": ["Aphids", "Termites", "Army worm"],
                    "diseases": ["Rust", "Powdery mildew", "Karnal bunt"]
                },
                "cotton": {
                    "name": "Cotton",
                    "scientific_name": "Gossypium",
                    "season": "Kharif (April-October)",
                    "water": "Moderate to high",
                    "soil": "Black cotton soil, deep",
                    "pests": ["Bollworm", "Whitefly", "Aphids"],
                    "diseases": ["Wilt", "Leaf curl", "Boll rot"]
                }
            },
            "pests": {
                "stem_borer": {
                    "name": "Stem Borer",
                    "scientific_name": "Scirpophaga incertulas",
                    "crop": "Rice",
                    "identification": "Dead hearts in vegetative stage, white ears in reproductive stage",
                    "organic": "Use Trichogramma egg parasitoids, neem-based pesticides",
                    "prevention": "Remove stubbles, avoid excessive nitrogen, maintain proper water level"
                },
                "bollworm": {
                    "name": "Bollworm",
                    "scientific_name": "Helicoverpa armigera",
                    "crop": "Cotton",
                    "identification": "Holes in bolls, larvae feeding inside",
                    "organic": "Use NPV (Nuclear Polyhedrosis Virus), neem oil spray",
                    "prevention": "Intercropping with marigold, pheromone traps, crop rotation"
                },
                "aphids": {
                    "name": "Aphids",
                    "scientific_name": "Aphis spp.",
                    "crop": "Wheat, Cotton, Vegetables",
                    "identification": "Small green/black insects on leaves and stems, sticky honeydew",
                    "organic": "Spray neem oil, introduce ladybugs, use soap solution",
                    "prevention": "Avoid over-fertilization, maintain field hygiene, use reflective mulch"
                }
            },
            "diseases": {
                "blast": {
                    "name": "Rice Blast",
                    "scientific_name": "Magnaporthe oryzae",
                    "crop": "Rice",
                    "symptoms": "Diamond-shaped lesions on leaves, neck rot",
                    "management": "Use resistant varieties, apply Tricyclazole fungicide",
                    "prevention": "Balanced fertilization, avoid water stress, proper spacing"
                },
                "rust": {
                    "name": "Wheat Rust",
                    "scientific_name": "Puccinia spp.",
                    "crop": "Wheat",
                    "symptoms": "Orange-brown pustules on leaves and stems",
                    "management": "Use resistant varieties, apply fungicides like Propiconazole",
                    "prevention": "Early sowing, remove volunteer plants, crop rotation"
                }
            }
        }
