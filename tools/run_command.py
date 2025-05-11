
import subprocess

def run_command(command: str) -> str:
    """Bir terminal komutu çalıştırır ve çıktısını döndürür."""
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Komut hatası: {e.output}"