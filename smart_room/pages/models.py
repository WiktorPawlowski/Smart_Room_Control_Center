from django.db import models


class RoomMode(models.Model):
    MODE_CHOICES = [
        ('GAMER', 'Gamer Mode'),
        ('STUDY', 'Study Mode'),
        ('CHILL', 'Chill Mode'),
        ('SLEEP', 'Sleep Mode'),
        ('STREAM', 'Stream Mode'),
    ]

    name = models.CharField(max_length=50, choices=MODE_CHOICES, unique=True)
    description = models.TextField(blank=True)
    led_color_hex = models.CharField(max_length=7, default="#FFFFFF")  # np. #FF0000
    brightness = models.IntegerField(default=50)  # 0-100%
    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Jeśli ten tryb jest aktywny, wyłącz wszystkie inne
        if self.is_active:
            RoomMode.objects.exclude(id=self.id).update(is_active=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({'ON' if self.is_active else 'OFF'})"


class Device(models.Model):
    name = models.CharField(max_length=100)  # np. "Główna Lampa", "PC"
    device_type = models.CharField(max_length=50)  # np. "LIGHT", "PC", "FAN"
    is_on = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class SensorLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()

    class Meta:
        ordering = ['-timestamp']