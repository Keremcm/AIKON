
import requests


def get_weather(location: str) -> str:
    """
    Belirtilen konum için hava durumu bilgisini döndürür.
    OpenWeatherMap API'sini kullanır.
    
    Args:
        location (str): Hava durumu bilgisi alınacak konum (şehir adı).
    
    Returns:
        str: Hava durumu bilgisi veya hata mesajı.
    """
    try:
        # OpenWeatherMap API bilgileri
        API_KEY = "1a44ca0976662f6f21b9cab1af1db067"  # OpenWeatherMap API anahtarınızı buraya ekleyin
        BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

        # API isteği
        params = {
            "q": location,
            "appid": API_KEY,
            "units": "metric",  # Sıcaklık birimi: Celsius
            "lang": "tr"       # Dil: Türkçe
        }
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # HTTP hatalarını kontrol et

        # API yanıtını işle
        data = response.json()
        city = data["name"]
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]

        # Hava durumu bilgisi
        return f"{city} için hava durumu: {temp}°C, {weather.capitalize()}."

    except requests.exceptions.RequestException as e:
        return f"[!] Hava durumu bilgisi alınamadı: {e}"
    except KeyError:
        return "[!] Hava durumu bilgisi alınamadı. Konumu kontrol edin."