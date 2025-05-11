import os, pygame, tempfile
from gtts import gTTS

def speech(text: str) -> str:
    """Verilen metni sesli olarak okur."""
    konuş = text.replace("*", "")
    tts = gTTS(text=konuş, lang='tr')
    with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as fp:
        temp_path = fp.name
    tts.save(temp_path)
    pygame.mixer.music.load(temp_path)
    pygame.mixer.music.play()

    # Sesin bitmesini bekle
    while pygame.mixer.music.get_busy():
        continue
