from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Automatyczne tworzenie ścieżek API
router = DefaultRouter()
router.register(r'modes', views.RoomModeViewSet)
router.register(r'devices', views.DeviceViewSet)
router.register(r'sensors', views.SensorLogViewSet)

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Strona główna
    path('api/', include(router.urls)),  # Endpointy API np. /api/modes/
    path('wallboard/', views.wallboard, name='wallboard'),

    # 👇 TUTAJ BYŁ BŁĄD: Zmieniłem 'get_calendar_events' na 'calendar_events'
    path('api/calendar/', views.calendar_events, name='calendar-events'),
]