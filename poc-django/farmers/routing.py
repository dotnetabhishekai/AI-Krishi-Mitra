"""WebSocket routes for farmers app."""
from django.urls import re_path

from .consumers import TranscribeConsumer

websocket_urlpatterns = [
    re_path(r'^ws/transcribe/$', TranscribeConsumer.as_asgi()),
]
