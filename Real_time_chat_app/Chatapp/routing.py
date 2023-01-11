from django.urls import path
from . import consumers
    

websocket_urlpatterns = [
    # path('ws/sc/',consumers.MySyncConsumer.as_asgi()),
    # path('ws/ac/',consumers.MyAsyncConsumer.as_asgi()),
    path('ws/sc/<str:userName>/',consumers.MySyncConsumer.as_asgi()),
    path('ws/ac/<str:userName>/',consumers.MyAsyncConsumer.as_asgi()),
]