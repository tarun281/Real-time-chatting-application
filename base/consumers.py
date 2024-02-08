import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User

from base.models import Chat, Room

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnet(self):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_layer
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']

        await self.save_messages(username, room, message)

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type':'chat_message',
                'message':message,
                'username':username,
                'room':room
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        room = event['room']

        await self.send(text_data=json.dumps({
            'message':message,
            'username':username,
            'room':room
        }))
    @sync_to_async
    def save_messages(self, username, room, message):
        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room)
        
        Chat.objects.create(user=user, room=room, message=message)