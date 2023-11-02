# chat/consumers.py
from typing import Dict

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.template.loader import get_template

from advanced_htmx.constants import CHAT_WS_GROUP_NAME


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            CHAT_WS_GROUP_NAME,
            self.channel_name,
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            CHAT_WS_GROUP_NAME,
            self.channel_name,
        )

    def chat_message(self, event: Dict[str, str]):
        html = get_template(
            "advanced_htmx/mini_partials/chat_messages_container.html",
        ).render(
            context={
                "messages": [
                    event["message"],
                ]
            }
        )

        self.send(text_data=html)
