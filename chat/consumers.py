import json
import uuid
from channels.generic.websocket import AsyncWebsocketConsumer

# Simple in-memory queue (OK for demo & interview)
waiting_users = []

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()
        self.room_name = None
        print("CONNECTED", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)

        # 🔵 Start matchmaking
        if data.get("type") == "start":
            if self not in waiting_users:
                waiting_users.append(self)

            if len(waiting_users) >= 2:
                user1 = waiting_users.pop(0)
                user2 = waiting_users.pop(0)

                room = str(uuid.uuid4())

                await user1.join_room(room, True)
                await user2.join_room(room, False)

        # 🔵 Next button → leave + requeue
        elif data.get("type") == "next":
            if self.room_name:
                await self.channel_layer.group_discard(
                    self.room_name,
                    self.channel_name
                )
                self.room_name = None

            if self not in waiting_users:
                waiting_users.append(self)

            if len(waiting_users) >= 2:
                user1 = waiting_users.pop(0)
                user2 = waiting_users.pop(0)

                room = str(uuid.uuid4())

                await user1.join_room(room, True)
                await user2.join_room(room, False)

        # 🔵 WebRTC signaling relay
        elif data.get("room"):
            await self.channel_layer.group_send(
                data["room"],
                {
                    "type": "relay",
                    "message": data
                }
            )

    async def join_room(self, room, initiator):
        self.room_name = room

        await self.channel_layer.group_add(
            room,
            self.channel_name
        )

        await self.send(json.dumps({
            "type": "matched",
            "room": room,
            "initiator": initiator
        }))

    async def relay(self, event):
        await self.send(json.dumps(event["message"]))

    async def disconnect(self, close_code):
        if self in waiting_users:
            waiting_users.remove(self)

        if self.room_name:
            await self.channel_layer.group_discard(
                self.room_name,
                self.channel_name
            )

        print("DISCONNECTED", self.channel_name)
