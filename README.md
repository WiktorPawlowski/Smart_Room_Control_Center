📘 Smart Room Control Center 2.0

Inteligentny Asystent Pokoju oparty o Raspberry Pi 5, Web App, Mobile App i AI

⸻

🚀 Opis projektu

Smart Room Control Center 2.0 to zaawansowany system typu smart home zaprojektowany specjalnie dla pokoju nastolatka. Projekt łączy:
    •    Raspberry Pi 5 jako centrum sterowania
    •    aplikację mobilną
    •    panel webowy
    •    backend z API i bazą danych
    •    moduły automatyzacji i AI

System umożliwia pełne zarządzanie pokojem: oświetleniem, muzyką, trybami użytkownika, bezpieczeństwem oraz informacjami wyświetlanymi na ekranie.

⸻

🌟 Najważniejsze funkcje

🎭 Tryby Osobowości Pokoju (Room Personas)

Gotowe sceny:
    •    GAMER MODE – RGB, ciemne światło, powiadomienia OFF
    •    STUDY MODE – jasne światło, fokus, minimalizacja rozpraszaczy
    •    CHILL MODE – ciepłe światło i muzyka lo-fi
    •    SLEEP MODE – automatyczne wygaszanie LED
    •    STREAM MODE – oświetlenie studyjne do kamerki

Każdy tryb steruje światłem, muzyką, urządzeniami i powiadomieniami.

⸻

💡 Inteligentne oświetlenie LED
    •    animacje i efekty świetlne
    •    tryb audio-reactive
    •    kontrola jasności, barwy i scen
    •    sterowanie przez aplikację mobilną

⸻

📺 WallBoard – interaktywny ekran informacyjny

Raspberry Pi wyświetla:
    •    plan lekcji
    •    pogodę
    •    powiadomienia
    •    przypomnienia
    •    mood-indicator (kolor LED zależny od nastroju)

⸻

🤖 Asystent AI

AI analizuje zachowania i sugeruje automatyzacje, np.:
    •    „Masz jutro sprawdzian — proponuję Study Mode.”
    •    „Widzę, że streamujesz — włączam Stream Mode.”

⸻

🖥️ Integracja z komputerem (opcjonalnie)
    •    monitor temperatur CPU/GPU
    •    sterowanie RGB PC
    •    tryb Focus blokujący rozpraszacze
    •    automatyczne zmiany tapety w zależności od trybu

⸻

🔐 System bezpieczeństwa
    •    kamera z wykrywaniem ruchu
    •    rozpoznawanie twarzy (właściciel / gość)
    •    alerty push na telefon
    •    tryb prywatności: kamera/mikrofon OFF

⸻

📱 Aplikacja mobilna
    •    sterowanie trybami i scenami
    •    pilot LED
    •    panel muzyki
    •    odbieranie alertów
    •    personalizacja pokoju

⸻

🧭 Dashboard Web
    •    wykresy użycia trybów
    •    statystyki zachowań
    •    edytor scen (drag & drop)
    •    zarządzanie kontem i urządzeniami

⸻
🏗️ Architektura systemu
                ┌─────────────────┐
                │  Mobile App     │
                └──────▲──────────┘
                       │ REST / WS
                ┌──────▼──────────┐
                │   Backend API    │
                └──────▲──────────┘
                       │
            ┌──────────▼─────────┐
            │   Database (SQL)    │
            └──────────▲─────────┘
                       │
   ┌───────────────────▼────────────────────┐
   │             Raspberry Pi 5             │
   │  - LED controller                      │
   │  - audio-reactive engine               │
   │  - camera & face detection             │
   │  - WallBoard display                   │
   └────────────────────────────────────────┘

                ┌───────────────────┐
                │  Web Dashboard    │
                └───────────────────┘

⸻

🛠️ Technologie

Frontend:
    •    React Native
    •    React / Next.js
    •    TailwindCSS

Backend:
    •    Node.js / Express lub Python / FastAPI
    •    WebSockety
    •    JWT Auth

Baza danych:
    •    PostgreSQL / MongoDB

Raspberry Pi:
    •    Python
    •    OpenCV
    •    GPIO / PWM
    •    obsługa kamer i LED

AI:
    •    TensorFlow Lite / lokalne modele NLP
    •    rozpoznawanie twarzy
    •    analiza tekstu i nastrojów


⸻

📌 Status projektu

Projekt w trakcie aktywnego rozwoju (2024/2025).

⸻

🤝 Współtwórz

Pull Requesty i Issues mile widziane.

⸻

📄 Licencja

MIT

⸻

👤 Autor

Wiktor Pawłowski

⸻
