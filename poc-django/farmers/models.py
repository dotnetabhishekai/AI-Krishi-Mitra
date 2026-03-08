"""
Models for farmers app
"""
from django.db import models
from django.contrib.auth.models import User


class FarmerProfile(models.Model):
    """Farmer profile model"""
    APPROVAL_STATUS = [
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='farmer_profile')
    phone_number = models.CharField(max_length=15, unique=True)
    location = models.CharField(max_length=200, default='Unknown')
    state = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)
    crops = models.JSONField(default=list)  # List of crops
    farm_size = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # in hectares
    language = models.CharField(max_length=10, default='en', choices=[
        ('en', 'English'),
        ('hi', 'Hindi'),
        ('te', 'Telugu'),
        ('ta', 'Tamil'),
        ('mr', 'Marathi'),
        ('kn', 'Kannada'),
        ('bn', 'Bengali'),
        ('gu', 'Gujarati'),
    ])
    approval_status = models.CharField(max_length=20, choices=APPROVAL_STATUS, default='pending')
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_farmers')
    approved_at = models.DateTimeField(null=True, blank=True)
    rejection_reason = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'farmer_profiles'
        verbose_name = 'Farmer Profile'
        verbose_name_plural = 'Farmer Profiles'
    
    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} - {self.phone_number}"


class Conversation(models.Model):
    """Conversation/Chat session model"""
    farmer = models.ForeignKey(FarmerProfile, on_delete=models.CASCADE, related_name='conversations')
    title = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'conversations'
        ordering = ['-updated_at']
        verbose_name = 'Conversation'
        verbose_name_plural = 'Conversations'
    
    def __str__(self):
        return f"Conversation {self.id} - {self.farmer.user.username}"


class Message(models.Model):
    """Individual message in a conversation"""
    MESSAGE_TYPES = [
        ('text', 'Text'),
        ('voice', 'Voice'),
        ('image', 'Image'),
    ]
    
    SENDER_TYPES = [
        ('farmer', 'Farmer'),
        ('ai', 'AI Assistant'),
    ]
    
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender_type = models.CharField(max_length=10, choices=SENDER_TYPES)
    message_type = models.CharField(max_length=10, choices=MESSAGE_TYPES, default='text')
    content = models.TextField()
    audio_file = models.FileField(upload_to='audio/', null=True, blank=True)
    image_file = models.ImageField(upload_to='images/', null=True, blank=True)
    metadata = models.JSONField(default=dict, blank=True)  # Additional data
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'messages'
        ordering = ['created_at']
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
    
    def __str__(self):
        return f"{self.sender_type}: {self.content[:50]}"


class Interaction(models.Model):
    """Track farmer interactions for analytics"""
    farmer = models.ForeignKey(FarmerProfile, on_delete=models.CASCADE, related_name='interactions')
    interaction_type = models.CharField(max_length=50)  # query, weather, crop_advice, etc.
    query = models.TextField()
    response = models.TextField(blank=True)
    duration_seconds = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'interactions'
        ordering = ['-created_at']
        verbose_name = 'Interaction'
        verbose_name_plural = 'Interactions'
    
    def __str__(self):
        return f"{self.farmer.user.username} - {self.interaction_type}"


class WeatherData(models.Model):
    """Cache weather data"""
    location = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.IntegerField()
    rainfall = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    conditions = models.CharField(max_length=100)
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    forecast_data = models.JSONField(default=list, blank=True)
    fetched_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'weather_data'
        verbose_name = 'Weather Data'
        verbose_name_plural = 'Weather Data'
    
    def __str__(self):
        return f"{self.location} - {self.temperature}°C"
