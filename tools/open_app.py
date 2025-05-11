import os, subprocess, difflib, threading

def find_installed_apps():
    """Bilgisayarda bulunan tüm uygulamaları arar ve listeler."""
    apps = []
    paths = [
        os.path.join(os.environ.get('ProgramFiles',''), ''),
        os.path.join(os.environ.get('ProgramFiles(x86)',''), ''),
        os.path.join(os.environ.get('APPDATA',''), 'Microsoft', 'Windows', 'Start Menu', 'Programs'),
        os.path.join(os.environ.get('USERPROFILE',''), 'Desktop')
    ]
    for p in paths:
        for root, dirs, files in os.walk(p):
            for f in files:
                if f.lower().endswith('.exe'):
                    apps.append((f[:-4], os.path.join(root,f)))
    return apps

def open_app(uygulama_adi: str) -> str:
    """Verilen uygulama adını bilgisayarda aratır. En yakın uygulamayı terminal kullanarak çalıştırır."""
    apps = find_installed_apps()
    match = difflib.get_close_matches(uygulama_adi, [a[0] for a in apps], n=1)
    if match:
        for n, path in apps:
            if n == match[0]:
                threading.Thread(target=subprocess.Popen, args=([path],), kwargs={'shell':True}).start()
                return f"{n} başlatıldı."
    return f"{uygulama_adi} bulunamadı."