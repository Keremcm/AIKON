from bs4 import BeautifulSoup
import requests

def web_search(query: str) -> str:
    """DuckDuckGo'da arama yapar, ilk 3 sonucu çözüp içeriklerini çeker."""
    try:
        url = f"https://duckduckgo.com/html/?q={query}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        links = soup.select('a.result__a')
        results = []

        for link in links[:3]:  # İlk 3 linki işle
            title = link.get_text()
            href = link.get('href')

            # DuckDuckGo yönlendirmesini çöz
            if href.startswith("//duckduckgo.com/l/?uddg="):
                real_url = href.split("uddg=")[1]
                real_url = requests.utils.unquote(real_url)
                if not real_url.startswith("http"):
                    real_url = "https:" + real_url
            else:
                real_url = href

            try:
                page = requests.get(real_url, timeout=10)
                content = BeautifulSoup(page.text, 'html.parser').get_text(separator="\n", strip=True)[:3000]
            except requests.exceptions.RequestException as e:
                content = f"Hata oluştu: {str(e)}"

            results.append(f"🔗 {title} - {real_url}\n{content}\n{'='*80}")

        return "\n".join(results) if results else "Sonuç bulunamadı."

    except Exception as e:
        return f"Genel hata: {str(e)}"