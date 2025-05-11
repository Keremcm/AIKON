#!/usr/bin/env bash
#############################################################################
#                                                                             #
#   █████╗ ██╗ ██████╗ ██╗  ██╗ ██████╗ ██╗  ██╗  Autonomous Intelligence      #
#  ██╔══██╗██║██╔═══██╗██║ ██╔╝██╔═══██╗██║  ██║  Kernel of Neural Systems    #
#  ███████║██║██║   ██║█████╔╝ ██║   ██║███████║                                  #
#  ██╔══██║██║██║   ██║██╔═██╗ ██║   ██║██╔══██║   “AIKON devrede. Talimat      #
#  ██║  ██║██║╚██████╔╝██║  ██╗╚██████╔╝██║  ██║    bekleniyor veya kendi        #
#  ╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝    görevlerini üstlenmeye      #
#                                  hazır.”                                   #
#                                                                             #
#############################################################################

▶ Proje: AIKON – Autonomous Intelligence Kernel of Neural Systems
▶ Versiyon: v2.0.0
▶ Yazar  : Master Chief (Keremcem Kaysi)
▶ İletişim: keremcem0120@hotmail.com

─────────────────────────────────────────────────────────────────────────────

 ⁂ Açıklama:
    AIKON, LangChain & Ollama tabanlı, tamamen otonom bir asistan. 
    - Kullanıcı komutlarını alır.
    - Kendi kendine görev oluşturur ve yürütür.
    - Sonuçları anlık olarak bildirir.

─────────────────────────────────────────────────────────────────────────────

 ⁂ Özellikler:
    • Web & Wikipedia Arama  
    • Dosya Okuma/Yazma/Açma/Arama  
    • Hava Durumu & Trafik Bilgisi  
    • Kamera Görüntüsü Analizi  
    • Medya Oynatma/Durdurma/Atlama  
    • Grafik Üretimi (Metin→Grafik)  
    • Takvim Etkinlik Yönetimi  
    • Telegram Botu Entegrasyonu  
    • Terminal Komut Yürütme  
    • Sesli Okuma

─────────────────────────────────────────────────────────────────────────────

 ⁂ Kurulum & Başlangıç:
    1) Depoyu klonlayın:
       git clone https://github.com/Keremcm/AIKON.git && cd AIKON

    2) Gerekli kütüphaneler:
       pip install -r requirements.txt

    3) API anahtarları:
       - tools/get_weather.py → YOUR_OPENWEATHER_API_KEY
       - main.py → TELEGRAM_BOT_TOKEN & USER_ID

    4) Ollama modelini indirin:
       ollama serve & ollama pull Keremcm_/Asistan_AI:12b

    5) AIKON'u başlatın:
       python main.py

─────────────────────────────────────────────────────────────────────────────

 ⁂ Kullanım Örnekleri:
    $ web_search: “Python nedir?”  
    $ get_weather: Istanbul  
    $ write_to_file: “Merhaba Dünya!”  
    $ camera_vision  
    $ task: “Günlük rapor hazırla”

─────────────────────────────────────────────────────────────────────────────

 ⁂ Proje Yapısı:
    AIKON/
    ├── main.py
    ├── tools/
    │   ├── camera_vision.py
    │   ├── calendar_tools.py
    │   ├── file_tools.py
    │   ├── get_weather.py
    │   ├── media_control.py
    │   ├── production_graphic.py
    │   ├── telegram_tools.py
    │   ├── trafic_data.py
    │   ├── web_search.py
    │   └── wikipedia_search.py
    ├── context_log.json
    ├── memory.json
    ├── takvim.json
    └── README.md

─────────────────────────────────────────────────────────────────────────────

 ⁂ Notlar:
    • “ollama serve” arka planda çalışmalı.  
    • Platform uyumluluğu için alternatif komutlara göz atın.  
    • Tüm işlemler context_log.json’a kaydedilir.

─────────────────────────────────────────────────────────────────────────────

 ⁂ Katkıda Bulunma:
    git fork → git checkout -b feature/isim → commit → push → Pull Request

─────────────────────────────────────────────────────────────────────────────

 “AIKON ile geleceği şimdi yürüt. Let intelligence lead.”  

#############################################################################
