from urllib.parse import urlparse
import requests, datetime, os, json


BOT_TOKEN = "8023242841:AAFXUhTwu_23DS_L9GlBAmYkWc2F46shbos"
USER_ID = 6769405767  # Sadece bu ID'den mesaj al
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"
last_update_id = None

def send_telegram(text: str) -> str:
    """Telegram botu ile kullanıcıya mesaj gönderir."""
    response = requests.post(f"{BASE_URL}/sendMessage", data={
        "chat_id": USER_ID,
        "text": text
    })
    return response.text

def control_telegram() -> str:
    """
    Telegram'dan, kullanıcı tarafından gelen son cevaplanmamış mesajı kontrol eder ve döner.
    """
    global last_update_id

    url = f"{BASE_URL}/getUpdates"
    if last_update_id:
        url += f"?offset={last_update_id + 1}"

    try:
        res = requests.get(url).json()
        if res["ok"] and res["result"]:
            for update in res["result"]:
                last_update_id = update["update_id"]
                msg = update.get("message", {})
                chat_id = msg.get("chat", {}).get("id")
                text = msg.get("text", "")

                # Sadece kullanıcıdan gelen mesajları kontrol et
                if chat_id == USER_ID and text:
                    return text

        return "Cevaplanmamış mesaj bulunamadı."

    except Exception as e:
        return f"Telegram kontrolü sırasında hata oluştu: {e}"
