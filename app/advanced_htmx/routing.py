# chat/routing.py
from django.urls import path

from advanced_htmx.consumers import ChatConsumer

websocket_urlpatterns = [
    path(r"ws/chatroom", ChatConsumer.as_asgi()),
]
