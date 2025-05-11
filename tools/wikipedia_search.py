import requests

def wikipedia_search_tool(query: str) -> str:
    """Wikipedia API'si ile verilen sorgu hakkında bilgi alır. JSON string alır."""
    try:
        # Wikipedia API'sine sorgu gönder
        url = "https://tr.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": query,
            "utf8": 1,
            "srlimit": 1
        }
        
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            search_results = data["query"]["search"]
            
            # İlk sonucu özetle
            result_str = ""
            for result in search_results:
                result_str += f"Başlık: {result['title']}\nÖzet: {result['snippet']}\n\n"
                
            if result_str:
                return result_str
            else:
                return "Hiçbir sonuç bulunamadı."
        else:
            return "Wikipedia API'ye bağlanılamadı."
    except Exception as e:
        return f"[!] Hata: {e}"