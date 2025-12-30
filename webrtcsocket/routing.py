from django.urls import re_path
from .consumers import ChatConsumer

# WebSocket endpoint
websocket_urlpatterns = [
    re_path(r"ws/chat/$", ChatConsumer.as_asgi()),
]
