"""ASGI config for krishi_mitra project."""
import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'krishi_mitra.settings')

# Initialize Django ASGI app early to ensure AppRegistry is loaded.
django_asgi_app = get_asgi_application()

from .routing import websocket_urlpatterns  # noqa: E402

application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': AuthMiddlewareStack(URLRouter(websocket_urlpatterns)),
})
