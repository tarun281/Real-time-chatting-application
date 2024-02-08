from django.urls import path
from base.consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/<str:room_name>/',ChatConsumer.as_asgi())
]