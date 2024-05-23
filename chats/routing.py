from django.urls import re_path

from chats import consumers

ws_urlpatterns = [
    re_path(r'ws/chats/chat/(?P<uuid>[0-9a-f-]{36})/$', consumers.ChatConsumer.as_asgi()),
]
