def write_to_file(content: str) -> str:
    """Verilen veriyi bir dosyaya yazar. JSON formatında bir input alır."""
    try:
        file_name = "output.txt"  # Varsayılan dosya adı
        content = content
        
        # İçeriği dosyaya yaz
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(content)
            
        return f"[+] '{file_name}' dosyasına başarıyla yazıldı."
    except Exception as e:
        return f"[!] Dosyaya yazma hatası: {e}"