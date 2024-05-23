import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth import get_user_model

from chats.models import Group, Message

User = get_user_model()


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_uuid = self.scope['url_route']['kwargs']['uuid']
        self.room_group_name = 'chat_%s' % self.room_uuid

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json.get('username', None)

        user = User.objects.get(username=username)
        group = Group.objects.get(uuid=self.room_uuid)

        db_insert = Message(author=user, content=message, group=group)
        db_insert.save()

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {'type': 'chat_message', 'message': f'{message}'}
        )

    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({'message': message}))
