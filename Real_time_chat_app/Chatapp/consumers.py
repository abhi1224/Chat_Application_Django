from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from .models import*
from time import sleep
import asyncio
import json
from channels.db import database_sync_to_async

# added
from cryptography.fernet import Fernet 


class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('Websocket connect ....',event)
        print("Channels layer ...",self.channel_layer)
        print("Channels name ...",self.channel_name)
        print(self.scope['url_route']['kwargs']['userName'])
        self.user_name = self.scope['url_route']['kwargs']['userName']
        async_to_sync(self.channel_layer.group_send)(
            self.user_name,
            self.channel_name
            )         
        self.send({
            'type':'websocket.accept'
        })
  

    def websocket_receive(self, event):
        print('websocket Received ...',event)
        print('websocket Received from client...',event['text'])
        async_to_sync(self.channel_layer.group_send)(
            self.user_name,  
        {
            'type': 'chat.message',
            'message': event['text']
        })
        print(event['text'])

    def chat_message(self, event):
        print('event...',event)
        self.send({
            'type':'websocket.send',
            'text':event['message']
        })            

    def websocket_disconnect(self,event):
        print('websocket Disconnected ...',event)
        async_to_sync(self.channel_layer.group_discard)(
            self.user_name,
            self.channel_name
        )
        raise StopConsumer()



# added
# class MyAsyncConsumer(AsyncConsumer):  
      
#     async def websocket_connect(self,event):
#         print('Websocket connect ....')
#         print('Websocket connect ....',event)
#         print(self.scope['url_route']['kwargs']['userName'])
#         self.user_name = self.scope['url_route']['kwargs']['userName']
#         await self.channel_layer.group_add(
#             self.user_name,
#             self.channel_name
#             )  

#         await self.send({
#             'type':'websocket.accept'
#         })

#     async def websocket_receive(self,event):
#         print('websocket Received ...')
#         print('websocket Received ...',event)
#         data = json.loads(event['text'])

#         key = Fernet.generate_key()
#         fernet = Fernet(key)
#         encMessage = fernet.encrypt(event['text'].encode())
#         print("original string: ", event['text'])
#         print("encrypted string: ", encMessage)
#         decMessage = fernet.decrypt(encMessage).decode()
#         print("decrypted string: ", decMessage)

#         # data = json.loads(event['text'])
#         group = await database_sync_to_async (Group.objects.get)(name=self.user_name)
#         chat = Chat(
#             content = encMessage,
#             # content = data['msg'],
#             group = group
#         )
#         await database_sync_to_async(chat.save)()
#         await self.channel_layer.group_send(
#           self.user_name,  
#         {
#             'type': 'chat.message',
#             # 'message':event['text']
#             'message': decMessage
#         }
#         )

#     async def chat_message(self,event):
#         print('event...',event)
#         await self.send({
#             'type':'websocket.send',
#             'text':event['message']

#         })
        
#     async def websocket_disconnect(self,event):
#         print('websocket Disconnected ...')
#         raise StopConsumer()











class MyAsyncConsumer(AsyncConsumer):  
      
    async def websocket_connect(self,event):
        print('Websocket connect ....')
        print('Websocket connect ....',event)
        print(self.scope['url_route']['kwargs']['userName'])
        self.user_name = self.scope['url_route']['kwargs']['userName']
        await self.channel_layer.group_add(
            self.user_name,
            self.channel_name
            )  

        await self.send({
            'type':'websocket.accept'
        })

    async def websocket_receive(self,event):
        print('websocket Received ...')
        print('websocket Received ...',event)
        await self.channel_layer.group_send(
          self.user_name,  
        {
            'type': 'chat.message',
            'message':event['text']
        }
        )

    async def chat_message(self,event):
        print('event...',event)
        await self.send({
            'type':'websocket.send',
            'text':event['message']
        })
        
    async def websocket_disconnect(self,event):
        print('websocket Disconnected ...')
        raise StopConsumer()









