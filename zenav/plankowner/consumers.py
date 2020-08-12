import json
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth import get_user_model
from .models import Device, Driver, Talent

from djangochannelsrestframework import permissions
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import ListModelMixin, UpdateModelMixin, PatchModelMixin
# , CreateModelMixin, DeleteModelMixin
from djangochannelsrestframework.observer.generics import ObserverModelInstanceMixin
from channelsmultiplexer import AsyncJsonWebsocketDemultiplexer

from . import serializers


# class UserConsumer(ObserverModelInstanceMixin, ListModelMixin, GenericAsyncAPIConsumer):
#     queryset = get_user_model().objects.all()
#     serializer_class = serializers.UserSerializer
#     permission_classes = (permissions.IsAuthenticated,)


class DriverConsumer(ObserverModelInstanceMixin, ListModelMixin, GenericAsyncAPIConsumer):
    queryset = Driver.objects.all()
    serializer_class = serializers.DriverSerializer
    permission_classes = (permissions.IsAuthenticated,)


class DeviceConsumer(ObserverModelInstanceMixin, ListModelMixin, GenericAsyncAPIConsumer):
    queryset = Device.objects.all()
    serializer_class = serializers.DeviceSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TalentConsumer(ObserverModelInstanceMixin, ListModelMixin, UpdateModelMixin, PatchModelMixin, GenericAsyncAPIConsumer):
    queryset = Talent.objects.all()
    serializer_class = serializers.TalentSerializer
    permission_classes = (permissions.IsAuthenticated,)


class PanelDemultiplexerAsyncJson(AsyncJsonWebsocketDemultiplexer):
    applications = {
        "talentstream": TalentConsumer,
        "devicestream": DeviceConsumer,
        "driverstream": DriverConsumer
    }
