from datetime import datetime, timedelta
import requests, subprocess


def trafic_data(hedef: str) -> str:
    """Belirtilen hedef için trafik bilgisiyle rota hesaplar.

    Bu fonksiyon, kullanıcının başlangıç konumunu alır (PowerShell scripti ile),
    ardından hedef için TomTom API'sini kullanarak trafik bilgisiyle rota hesaplar ve
    yolculuk süresi, mesafe, trafik durumu gibi bilgileri döndürür.

    Args:
        hedef (str): Hedef konum adı (şehir, adres, vb.).

    Returns:
        str: Trafik durumu, mesafe, süre ve tahmini varış saati bilgilerini içeren bir metin.
    """
    API_KEY = "hD0HMKJ5t7BY7BnKTVLLiqW2ZGHMjFD9"
    result = subprocess.run(["powershell", "-Command", 'C:\\Users\\CASPER\\repos\Otonom\\V2\Otonom\\tools\\script.ps1'], capture_output=True, text=True)
    output = result.stdout.strip()
    if output:
        start_lat, start_lon = map(float, output.split(","))
    else:
        print("Konum alınamadı.")
        return "Konum alınamadı."
    search_url = f"https://api.tomtom.com/search/2/geocode/{hedef}.json?key={API_KEY}"
    response = requests.get(search_url).json()
    try:
        hedef_lat = response['results'][0]['position']['lat']
        hedef_lon = response['results'][0]['position']['lon']
        hedef_adres = response['results'][0]['address']['freeformAddress']
    except Exception:
        print("Hedef konum bulunamadı.")
        return "Hedef konum bulunamadı."
    route = requests.get(
        f"https://api.tomtom.com/routing/1/calculateRoute/"
        f"{start_lat},{start_lon}:{hedef_lat},{hedef_lon}/json?key={API_KEY}&traffic=true"
    ).json()
    try:
        summary = route['routes'][0]['summary']
        normal = summary['travelTimeInSeconds']//60
        delay = summary['trafficDelayInSeconds']//60
        total = (summary['travelTimeInSeconds']+summary['trafficDelayInSeconds'])//60
        dist = round(summary['lengthInMeters']/1000,2)
        yoğunluk = 'Yüksek' if delay>20 else 'Orta' if delay>10 else 'Düşük'
        varis = (datetime.datetime.now()+timedelta(minutes=total)).strftime('%H:%M')
        return (
            f"🗺️ Hedef: {hedef_adres} ({hedef_lat}, {hedef_lon})\n"
            f"📍 Mesafe: {dist} km\n"
            f"⏱️ Süre (trafiksiz): {normal} dk\n"
            f"🚦 Gecikme: {delay} dk ({yoğunluk})\n"
            f"🕒 Tahmini Varış: {varis}\n"
            f"➡️ Toplam: Yaklaşık {total} dk"
        )
    except Exception:
        return "Rota bilgisi alınamadı."
    