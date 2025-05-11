# Otonom Asistan Projesi

Otonom Asistan, çeşitli araçları (tools) kullanarak kullanıcıların günlük işlerini kolaylaştırmayı hedefleyen bir yapay zeka destekli asistan projesidir. Bu proje, yerel bir LLM (Large Language Model) olan **Ollama**'yı kullanarak doğal dil işleme yetenekleri sunar ve çeşitli araçlarla entegre çalışır.

---

## Özellikler

- **Web Arama**: İnternette arama yapar ve ilk sonuçları döndürür.
- **Wikipedia Arama**: Wikipedia üzerinde arama yapar ve sonuçları döndürür.
- **Dosya İşlemleri**: Dosya okuma, yazma, açma ve arama işlemleri yapar.
- **Hava Durumu**: Belirtilen bölge için hava durumu bilgisini sağlar.
- **Trafik Bilgisi**: Belirtilen hedefe trafik bilgisi ile rota hesaplar.
- **Kamera Görüntüsü Analizi**: Kamera görüntüsünü alır ve nesne tespiti yapar.
- **Medya Kontrolü**: Cihazda medya oynatma/durdurma/atlama işlemleri yapar.
- **Grafik Üretimi**: Metin formatındaki tabloyu grafik haline getirir.
- **Takvim İşlemleri**: Etkinlik oluşturma ve kontrol işlemleri yapar.
- **Telegram Botu**: Telegram üzerinden mesaj gönderir ve kontrol eder.
- **Komut Çalıştırma**: Terminal komutlarını çalıştırır ve çıktısını döndürür.
- **Sesli Okuma**: Verilen metni sesli olarak okur.

---

## Kurulum

### Gereksinimler

- Python 3.9 veya üzeri
- Gerekli Python kütüphaneleri:
  - `langchain`
  - `ultralytics`
  - `opencv-python-headless`
  - `numpy`
  - `pygame`
  - `tqdm`
  - `requests`
  - `matplotlib`
  - `pandas`

### Adımlar

1. **Depoyu Klonlayın**:
   ```bash
   git clone https://github.com/username/otonom-asistan.git
   cd otonom-asistan
   ```

2. **Gerekli Kütüphaneleri Yükleyin**:
   ```bash
   pip install -r requirements.txt
   ```

3. **OpenWeatherMap API Anahtarını Ekleyin**:
   - `tools/get_weather.py` dosyasındaki `API_KEY` değişkenine kendi OpenWeatherMap API anahtarınızı ekleyin.

4. **Telegram Botu Ayarları**:
   - `main.py` dosyasındaki `BOT_TOKEN` ve `USER_ID` değişkenlerini kendi Telegram botunuzun bilgileriyle değiştirin.

5. **Ollama Modelini İndirin**:
   - Ollama'yı kurun ve `Keremcm_/Asistan_AI:12b` modelini indirin.

---

## Kullanım

1. **Projeyi Başlatın**:
   ```bash
   python main.py
   ```

2. **Komut Gönderin**:
   - Terminalde komutlarınızı yazın ve asistanın yanıtlarını alın.

3. **Örnek Komutlar**:
   - **Web Arama**: `web_search: Python nedir?`
   - **Hava Durumu**: `get_weather: Istanbul`
   - **Dosya Yazma**: `write_to_file: Merhaba Dünya!`
   - **Kamera Görüntüsü**: `camera_vision`

---

## Proje Yapısı

```plaintext
Otonom/
├── main.py                 # Ana dosya
├── tools/                  # Araçlar (tools) klasörü
│   ├── __init__.py         # Araçların tanımlandığı dosya
│   ├── camera_vision.py    # Kamera görüntüsü analizi
│   ├── calendar_tools.py   # Takvim işlemleri
│   ├── file_tools.py       # Dosya okuma/yazma/açma/arama
│   ├── get_weather.py      # Hava durumu bilgisi
│   ├── log_case.py         # Loglama işlemleri
│   ├── media_control.py    # Medya kontrolü
│   ├── memory_tools.py     # Bellek yönetimi
│   ├── production_graphic.py # Grafik üretimi
│   ├── telegram_tools.py   # Telegram botu işlemleri
│   ├── trafic_data.py      # Trafik bilgisi
│   ├── web_search.py       # Web arama
│   ├── wikipedia_search.py # Wikipedia arama
│   ├── run_command.py      # Terminal komutları çalıştırma
│   ├── speech.py           # Metni sesli okuma
├── context_log.json        # Log dosyası
├── memory.json             # Bellek dosyası
├── takvim.json             # Takvim dosyası
└── README.md               # Proje açıklamaları
```

---

## Önemli Notlar

- **Ollama Modeli**: Ollama'nın düzgün çalışması için `ollama serve` komutunun arka planda çalıştığından emin olun.
- **Platform Uyumluluğu**: `os.startfile` gibi bazı fonksiyonlar yalnızca Windows'ta çalışır. Platform bağımsızlık için alternatif yöntemler kullanılabilir.
- **Loglama**: Tüm işlemler `context_log.json` dosyasına kaydedilir.

---

## Katkıda Bulunma

1. Bu projeyi fork edin.
2. Yeni bir dal oluşturun: `git checkout -b feature/ozellik-adi`
3. Değişikliklerinizi yapın ve commit edin: `git commit -m 'Yeni özellik eklendi'`
4. Dalınızı push edin: `git push origin feature/ozellik-adi`
5. Bir pull request oluşturun.

---

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakabilirsiniz.

---

## İletişim

Herhangi bir sorunuz veya öneriniz varsa, lütfen [keremcem0120@hotmail.com](mailto:keremcem0120@hotmail.com) adresinden iletişime geçin.