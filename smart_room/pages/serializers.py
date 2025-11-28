from rest_framework import serializers
from .models import RoomMode, Device, SensorLog

class RoomModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomMode
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class SensorLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorLog
        fields = '__all__'