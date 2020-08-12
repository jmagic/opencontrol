from rest_framework import serializers
from plankowner.models import Driver, Device, Talent


class DriverSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    authorized = serializers.ReadOnlyField()

    class Meta:
        model = Driver
        fields = ['name', 'owner', 'is_online', 'authorized', 'id', 'devices']


class DeviceSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    # driver = DriverSerializer()

    class Meta:
        model = Device
        fields = ['name', 'is_online', 'id', 'driver']


class TalentSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    # driver = DriverSerializer()

    class Meta:
        model = Talent
        fields = ['name', 'set_on', 'set_off', 'state', 'id', 'device']
