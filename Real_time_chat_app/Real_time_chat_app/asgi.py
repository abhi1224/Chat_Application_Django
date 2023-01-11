"""
ASGI config for Real_time_chat_app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
import Chatapp.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Real_time_chat_app.settings')

application = ProtocolTypeRouter({
    'http' : get_asgi_application(),
    'websocket' : URLRouter(
        Chatapp.routing.websocket_urlpatterns
    )
    })

