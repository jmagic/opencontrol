from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/driver/', consumers.DriverConsumer),
    re_path(r'ws/device/', consumers.DeviceConsumer),
    re_path(r'ws/talent/', consumers.TalentConsumer),
    re_path(r'ws/multi/', consumers.PanelDemultiplexerAsyncJson)
]
