import json

from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from django.contrib.auth import get_user_model

from chats.models import Group, Message

User = get_user_model()


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_uuid = self.scope['url_route']['kwargs']['uuid']
        self.room_group_name = 'chat_%s' % self.room_uuid

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    async def receive(self, text_data):
        """
        Receives a message from JavaScript, saves it to the database,
        and sends it to the chat group with the username in <strong> tags.

        Args:
            text_data (str): JSON text data message from JavaScript. Expected to contain 'message' and optionally 'username'.

        Example:
            text_data = '{"message": "Hello, world!", "username": "User123"}'
        """
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json.get('username')
        
        await save_message_to_db(username, message, self.room_uuid)

        await self.channel_layer.group_send(
            self.room_group_name, {'type': 'chat_message', 
                                   'message': message,
                                   'username': username}
        )

    async def chat_message(self, event):
        """
        Receives a chat message event from the group and sends it to the WebSocket.

        Args:
            event (dict): Event data containing the message to be sent to the WebSocket.
                          Expected to contain 'message'.

        Example:
            event = {'message': '<strong>User123</strong>: Hello, world!'}
        """
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({'message': message,
                                              'username': username}))


@database_sync_to_async
def save_message_to_db(username, message, room_uuid):
    group = Group.objects.get(uuid=room_uuid)
    user = User.objects.get(username=username)
    db_insert = Message(author=user, content=message, group=group)
    db_insert.save()
