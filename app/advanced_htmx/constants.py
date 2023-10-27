from enum import Enum

# Websockets
CHAT_WS_GROUP_NAME = "chatroom"


class EventType:
    chat_message = "chat_message"


class HTMXTriggers(Enum):
    products_list_page_changed = "products-list-page-changed"
