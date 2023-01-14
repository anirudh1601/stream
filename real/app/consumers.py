import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        await super().disconnect(close_code)

    # def receive(self, bytes_data):
    #     message=bytes_data
    #     print(message)