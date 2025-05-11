from datetime import datetime, timezone
import json, os

# Takvim dosyası
EVENTS_FILE = "takvim.json"

def calendar_create_local(input_text: str):
    """
    Etkinlik oluşturur ve yerel takvime ekler.
    Örnek: Doğum Günü:::2026-01-20:::19:37
    """
    try:
        parts = input_text.strip().split(":::")
        if len(parts) != 3:
            return "Giriş formatı hatalı. Doğru format: 'ETKİNLİK:::TARİH:::SAAT'"

        title, date_str, time_str = parts
        dt = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
        dt = dt.replace(tzinfo=timezone.utc)  # Offset-aware hale getir

        # Yeni etkinlik
        event = {
            "title": title,
            "datetime": dt.isoformat()  # ISO 8601 formatında kaydet
        }

        # Var olan etkinlikleri oku veya yeni bir liste oluştur
        if os.path.exists(EVENTS_FILE):
            with open(EVENTS_FILE, "r", encoding="utf-8") as f:
                events = json.load(f)
        else:
            events = []

        # Yeni etkinliği ekle
        events.append(event)

        # Güncellenmiş etkinlikleri dosyaya yaz
        with open(EVENTS_FILE, "w", encoding="utf-8") as f:
            json.dump(events, f, indent=4, ensure_ascii=False)

        return f"Etkinlik yerel takvime eklendi: {title} - {date_str} {time_str}"

    except Exception as e:
        return f"Hata oluştu: {e}"

def calendar_check_local():
    """
    Yerel takvim dosyasını kontrol eder ve en yakın etkinliği döndürür.
    """
    try:
        if not os.path.exists(EVENTS_FILE):
            return "Takvim dosyası bulunamadı."

        # Etkinlikleri oku
        with open(EVENTS_FILE, "r", encoding="utf-8") as f:
            events = json.load(f)

        now = datetime.now(timezone.utc)  # Offset-aware hale getir

        # Gelecek etkinlikleri filtrele ve sırala
        upcoming = sorted(
            [e for e in events if datetime.fromisoformat(e["datetime"]) >= now],
            key=lambda e: datetime.fromisoformat(e["datetime"])
        )

        if not upcoming:
            return f"Şu an: {now.strftime('%Y-%m-%d %H:%M')}\nYaklaşan etkinlik yok."

        next_event = upcoming[0]
        next_event_time = datetime.fromisoformat(next_event["datetime"])
        return (
            f"Şu an: {now.strftime('%Y-%m-%d %H:%M')}\n"
            f"En yakın etkinlik: {next_event['title']} - {next_event_time.strftime('%Y-%m-%d %H:%M')}"
        )

    except Exception as e:
        return f"Takvim kontrolü sırasında hata oluştu: {e}"