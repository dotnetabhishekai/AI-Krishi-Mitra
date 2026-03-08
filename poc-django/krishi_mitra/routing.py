"""Project-level websocket routing."""
from farmers.routing import websocket_urlpatterns as farmers_ws_patterns

websocket_urlpatterns = [*farmers_ws_patterns]
