from django.contrib import admin
from .models import RoomMode, Device, SensorLog

@admin.register(RoomMode)
class RoomModeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'led_color_hex', 'brightness')
    list_editable = ('is_active',)

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'device_type', 'is_on')
    list_editable = ('is_on',)

@admin.register(SensorLog)
class SensorLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'temperature', 'humidity')