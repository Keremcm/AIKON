import os, win32api, win32con


def media_control(command: str) -> str:
    """Alınan komuta göre cihazda medya kontorlü(durdur, devam ettir, atla, geri) yapar."""
    if "dur" in command or "duraklat" in command or "stop" in command:
        win32api.keybd_event(win32con.VK_MEDIA_PLAY_PAUSE, 0, 0, 0)  # Medyayı duraklat veya devam ettir
        return "Medya duraklatıldı."
    elif "devam" in command or "oynat" in command or "play" in command or "continue" in command:
        win32api.keybd_event(win32con.VK_MEDIA_PLAY_PAUSE, 0, 0, 0)  # Medyayı duraklat veya devam ettir
        return "Medya devam ettirildi."
    elif "atla" in command or "next" in command or "skip" in command:
        win32api.keybd_event(win32con.VK_MEDIA_NEXT_TRACK, 0, 0, 0)  # Sonraki parçaya atla
        return "Sonraki parçaya geçildi."
    elif "geri" in command or "previous" in command:
        win32api.keybd_event(win32con.VK_MEDIA_PREV_TRACK, 0, 0, 0)  # Önceki parçaya git
        return "Önceki parçaya geçildi."
    else:
        return "Anlaşılamadı."