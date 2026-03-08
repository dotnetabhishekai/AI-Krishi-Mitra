"""
URL configuration for farmers app
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Public pages
    path('', views.home, name='home'),
    
    # Authentication
    path('register/', views.register, name='register'),
    path('registration/pending/', views.registration_pending, name='registration_pending'),
    path('login/', auth_views.LoginView.as_view(template_name='farmers/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Farmer pages
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/setup/', views.profile_setup, name='profile_setup'),
    path('chat/', views.chat, name='chat'),
    path('chat/<int:conversation_id>/', views.chat, name='chat_with_id'),
    path('knowledge/', views.knowledge_base, name='knowledge'),
    path('weather/', views.weather_view, name='weather'),
    
    # API endpoints
    path('api/send-message/', views.send_message, name='send_message'),
    path('api/upload-voice/', views.upload_voice, name='upload_voice'),
    path('api/upload-image/', views.upload_image, name='upload_image'),
    path('api/transcribe-voice/', views.transcribe_voice_input, name='transcribe_voice_input'),
]
