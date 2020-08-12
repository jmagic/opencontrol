# from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import plankowner.routing
from .token_auth import TokenAuthMiddlewareStack

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': TokenAuthMiddlewareStack(
        URLRouter(
            plankowner.routing.websocket_urlpatterns
        )
    ),
})
