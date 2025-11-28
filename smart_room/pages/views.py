from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http import JsonResponse
import requests
import arrow
from ics import Calendar
from .models import RoomMode, Device, SensorLog
from .serializers import RoomModeSerializer, DeviceSerializer, SensorLogSerializer

# --- KONFIGURACJA KALENDARZA ---
# WAŻNE: Zastąp ten link swoim "Tajnym adresem w formacie iCal" z Google Calendar
ICAL_URL = "https://calendar.google.com/calendar/ical/wiktor.pawlowski%40infotech.edu.pl/private-603480a117c3a256a3ea2c36ccf68d42/basic.ics"


# --- API VIEWSETS ---

class RoomModeViewSet(viewsets.ModelViewSet):
    queryset = RoomMode.objects.all()
    serializer_class = RoomModeSerializer

    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        mode = self.get_object()
        mode.is_active = True
        mode.save()
        return Response({'status': f'{mode.name} activated'})

    @action(detail=False, methods=['get'])
    def current(self, request):
        active_mode = RoomMode.objects.filter(is_active=True).first()
        if active_mode:
            serializer = self.get_serializer(active_mode)
            return Response(serializer.data)
        return Response({'status': 'No active mode'}, status=404)


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class SensorLogViewSet(viewsets.ModelViewSet):
    queryset = SensorLog.objects.all()
    serializer_class = SensorLogSerializer


# --- WEB VIEWS ---

def dashboard(request):
    """Główny panel sterowania (sterowanie + wykresy)"""
    modes = RoomMode.objects.all()
    active_mode = RoomMode.objects.filter(is_active=True).first()
    devices = Device.objects.all()

    # Pobieramy najnowszy odczyt
    latest_sensor = SensorLog.objects.first()

    # Pobieramy 10 ostatnich odczytów do tabeli w statystykach
    recent_logs = SensorLog.objects.all().order_by('-timestamp')[:10]

    context = {
        'modes': modes,
        'active_mode': active_mode,
        'devices': devices,
        'sensor': latest_sensor,
        'recent_logs': recent_logs,
    }
    return render(request, 'pages/dashboard.html', context)


def wallboard(request):
    """Widok na ekran/monitor Raspberry Pi (Kiosk Mode)"""
    active_mode = RoomMode.objects.filter(is_active=True).first()
    latest_sensor = SensorLog.objects.first()
    context = {
        'active_mode': active_mode,
        'sensor': latest_sensor
    }
    return render(request, 'pages/wallboard.html', context)


# --- CALENDAR API ---

@api_view(['GET'])
def calendar_events(request):
    """
    Pobiera plik .ics z Google, przetwarza go i zwraca JSON
    z 5 najbliższymi wydarzeniami dla Wallboarda.
    """
    try:
        # 1. Pobierz plik kalendarza (timeout 5s żeby nie wisiało)
        response = requests.get(ICAL_URL, timeout=5)
        response.raise_for_status()

        c = Calendar(response.text)

        # 2. Znajdź nadchodzące wydarzenia
        events_data = []
        now = arrow.now()

        # Filtrujemy i sortujemy chronologicznie
        # (ics zwraca wszystkie wydarzenia, nawet te sprzed 5 lat, więc musimy filtrować)
        upcoming_events = sorted(c.events, key=lambda x: x.begin)

        for event in upcoming_events:
            event_end = arrow.get(event.end)

            # Bierzemy tylko te, które się jeszcze nie skończyły
            if event_end > now:
                # Konwersja do czasu lokalnego serwera
                start_time = arrow.get(event.begin).to('local')

                # Czy to wydarzenie całodniowe?
                if event.all_day:
                    time_str = "Cały dzień"
                    # Sprawdzenie daty dla całodniowych jest nieco inne
                    is_today = start_time.format('YYYY-MM-DD') == now.format('YYYY-MM-DD')
                else:
                    time_str = start_time.format('HH:mm')
                    is_today = start_time.date() == now.date()

                is_tomorrow = start_time.date() == now.shift(days=1).date()

                # Ładne nazwy dni
                if is_today:
                    day_str = "Dziś"
                elif is_tomorrow:
                    day_str = "Jutro"
                else:
                    # Np. "28.11"
                    day_str = start_time.format('DD.MM')

                events_data.append({
                    'name': event.name,
                    'time': time_str,
                    'day': day_str,
                    'is_today': is_today
                })

                # Ogranicz do 5 najbliższych wydarzeń
                if len(events_data) >= 5:
                    break

        return JsonResponse(events_data, safe=False)

    except Exception as e:
        # W razie błędu (np. brak neta) zwróć pustą listę lub błąd, żeby frontend nie padł
        print(f"Błąd kalendarza: {e}")
        return JsonResponse([], safe=False)