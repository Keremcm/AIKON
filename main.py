from langchain_community.llms import Ollama
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
import os, threading, subprocess, time, json, pygame, sys
from tqdm import tqdm
from datetime import datetime

# Yerel LLM (Ollama)
llm = Ollama(model="Keremcm_/Asistan_AI:12b", temperature=0.7)

def prepare_model():
    try:
        cmd = ["ollama", "serve"]
        kwargs = {"shell": False}
        if os.name == "nt":
            kwargs["creationflags"] = subprocess.CREATE_NO_WINDOW
        subprocess.run(cmd, **kwargs)
    except Exception:
        print("Ollama servisi başlatılamadı. Lütfen kontrol edin.")
        exit()
        
def loading_animation():
    """Dinamik bir yükleme animasyonu gösterir."""
    for _ in range(10):
        for char in "|/-\\":
            sys.stdout.write(f"\r\033[1;33mYükleniyor... {char}\033[0m")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r\033[1;32mYükleme tamamlandı!       \033[0m\n")
    
def print_boxed_message(message):
    """Mesajı çerçeve içinde yazdırır."""
    lines = message.split("\n")
    width = max(len(line) for line in lines)
    print("\033[1;34m" + "╔" + "═" * (width + 2) + "╗\033[0m")
    for line in lines:
        print("\033[1;34m║ \033[0m" + line.ljust(width) + " \033[1;34m║\033[0m")
    print("\033[1;34m" + "╚" + "═" * (width + 2) + "╝\033[0m")

# Sohbet geçmişi için bir değişken tanımla
conversation_history = ""

pygame.mixer.init()

# Telegram botu için gerekli ayarlar
BOT_TOKEN = "YOUR_BOT_TOKEN"
USER_ID = 6769405767  # Sadece bu ID'den mesaj al
last_update_id = None

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

EVENTS_FILE = "takvim.json"
MEMORY_FILE = "memory.json"

otonom = False  # Otonom mod başlangıçta kapalı

# Tool'ları içe aktar
from tools.camera_vision import camera_vision
from tools.calendar_tools import calendar_create_local, calendar_check_local
from tools.file_tools import read_file, write_to_file
from tools.media_control import media_control
from tools.production_graphic import production_grafic
from tools.telegram_tools import send_telegram, control_telegram
from tools.trafic_data import trafic_data
from tools.web_search import web_search
from tools.wikipedia_search import wikipedia_search_tool
from tools.get_weather import get_weather  # Yeni tool import edildi
from tools.open_app import open_app
from tools.speech import speech
from tools.run_command import run_command

# Tool'ları tanımla
tools = [
    Tool(name="web_search", func=web_search, description="İnternette arama yapar ve ilk sonuçları döner."),
    Tool(name="wikipedia_search_tool", func=wikipedia_search_tool, description="Wikipedia üzerinde arama yapar."),
    Tool(name="write_to_file", func=write_to_file, description="Verilen veriyi bir dosyaya yazar."),
    Tool(name="get_weather", func=get_weather, description="Belirtilen bölge için hava durumu bilgisini döndürür."),
    Tool(name="trafic_data", func=trafic_data, description="Belirtilen hedefe trafik bilgisi ile rota hesaplar."),
    Tool(name="camera_vision", func=camera_vision, description="Kamera görüntüsünü alır ve dosya yolunu verir."),
    Tool(name="open_app", func=open_app, description="Verilen uygulama adını bilgisayarda aratır. En yakın uygulamayı terminal kullanarak çalıştırır."),
    Tool(name="media_control", func=media_control, description="Alınan komuta göre cihazda medya kontorlü(durdur, devam ettir, atla, geri) yapar."),
    Tool(name="read_file", func=read_file, description="Verilen dosya yolundaki içeriği okur. Dosya yolu bilinmiyorsa dosya_ara ile önceden aratılmalıdır. Desteklenen formatlar: .json, .txt, .csv, .xlsx, .xls, .pdf."),
    Tool(name="production_grafic", func=production_grafic, description="Metin formatındaki tabloyu grafik haline getirir. Giriş şu şekilde olmalıdır: 'VERİ:::GRAFİK_TİPİ'. Desteklenen tipler: bar, line, pie. Grafik dosyası olarak 'grafik.png' üretilir."),
    Tool(name="send_telegram", func=send_telegram, description="Telegram botu ile kullanıcıya mesaj gönderir."),
    Tool(name="control_telegram", func=control_telegram, description="Telegram'dan, kullanıcı tarafından gelen son mesajı kontrol eder ve döner."),
    Tool(name="run_command", func=run_command, description="Bir terminal komutu çalıştırır ve çıktısını döndürür."),
    Tool(name="speech", func=speech, description="Verilen metni sesli olarak okur."),
    Tool(name="calendar_create_local", func=calendar_create_local, description="Etkinlik oluşturur ve yerel takvim dosyasına (takvim.ics) kaydeder. Giriş formatı: 'ETKİNLİK:::TARİH:::SAAT'"),
    Tool(name="calendar_check_local", func=calendar_check_local, description="Yerel takvim dosyasını kontrol eder ve en yakın etkinliği döndürür."),
]

# Agent başlat
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    max_iterations=None,
    max_execution_time=None,
    handle_parsing_errors=True
)

# Modeli başlat
threading.Thread(target=prepare_model, daemon=True).start()

# Terminal ekranını temizler
print("\033c", end="")
print("\033[2J\033[H", end="")

print("\033[38;5;117mAsistanNet başlatıldı. Komut gönderin veya çıkmak için Ctrl + C yapın.\033[0m")

# Sonsuz döngüde sürekli olarak kullanıcıdan girdi al
while True:
    # Kullanıcıdan giriş al
    user_input = input("\033[38;5;208m\n>>> \033[0m").strip()
    user_input = user_input + f"\n{datetime.now().strftime('%H:%M')}"
    model_active = True

    # Sohbet geçmişine kullanıcının girdisini ekle
    conversation_history += f"Siz: {user_input}\n"
    
    # Agent'e giriş ve geçmişi ver
    goal = conversation_history  # Daha önceki konuşmalarla birlikte

    # Yükleme animasyonu
    loading_animation()

    # Agent'i çalıştır ve çıktıyı al
    response = agent.invoke(goal)

    # Eğer response bir sözlükse, sadece 'output' anahtarını al
    if isinstance(response, dict) and "output" in response:
        response_text = response["output"]
    else:
        response_text = str(response)  # Eğer sözlük değilse, düz metin olarak al

    # Sadece son cevabı çerçeve içinde göster
    print_boxed_message(f"Asistan: {response_text}")
    conversation_history += f"Asistan: {response_text}\n"
    model_active = False

    # İlerleme çubuğu
    for _ in tqdm(range(100), desc="İşlem devam ediyor", ascii=True, ncols=75):
        time.sleep(0.01)