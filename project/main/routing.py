from asyncio.proactor_events import constants
from django.urls import re_path
from . import cons

websocket_urlpatterns = [
    re_path(r'ws/socket-server/', cons.Consumer.as_asgi())
]
