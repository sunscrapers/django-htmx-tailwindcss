from dataclasses import asdict
from dataclasses import dataclass
from typing import Dict
from typing import List

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from advanced_htmx.constants import CHAT_WS_GROUP_NAME
from advanced_htmx.constants import EventType


@dataclass
class ChatMessage:
    signature: str
    text: str

    def asdict(self):
        return asdict(self)


@dataclass
class EventChatMessage:
    type: EventType
    message: ChatMessage

    def asdict(self):
        return asdict(self)


tmp_messages_storage: List[ChatMessage] = [None for _ in range(10)]  # Store only ten latest messages


class ChatHandler:
    @classmethod
    def save_message(cls, message: ChatMessage):
        tmp_messages_storage.pop(0)
        tmp_messages_storage.append(message)

        cls.propagate_message(message=message)

    @classmethod
    def get_messages(cls) -> List[ChatMessage]:
        return [msg for msg in tmp_messages_storage if msg]

    @classmethod
    def get_messages_data(cls) -> List[Dict[str, str]]:
        return [msg.asdict() for msg in cls.get_messages()]

    @classmethod
    def propagate_message(cls, message: ChatMessage):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            CHAT_WS_GROUP_NAME,
            EventChatMessage(
                type=EventType.chat_message,
                message=message,
            ).asdict(),
        )
