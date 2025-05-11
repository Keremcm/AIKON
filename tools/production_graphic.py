import pandas as pd  # Veri işleme için
import matplotlib.pyplot as plt  # Grafik oluşturma için
import io  # Metin verisini bellek içi dosya gibi işlemek için


def production_grafic(veri_ve_tip: str) -> str:
    """
    Metin verisini grafik haline getirir.
    veri_ve_tip formatı: 'TÜM VERİ:::GRAFİK_TİPİ' (örnek: 'A,10\nB,20:::bar')
    Desteklenen grafik_tipleri: bar, line, pie
    Kaydedilen grafik dosyası: grafik.png
    """

    try:
        veri_str, grafik_tipi = veri_ve_tip.split(":::")
        df = pd.read_csv(io.StringIO(veri_str))

        if df.shape[1] != 2:
            return "❌ Veri 2 sütunlu olmalıdır. (Kategori, Değer)"

        kategori = df.iloc[:, 0]
        deger = df.iloc[:, 1]

        plt.figure(figsize=(8, 5))

        if grafik_tipi == "bar":
            plt.bar(kategori, deger, color="skyblue")
            plt.title("Bar Grafiği")

        elif grafik_tipi == "line":
            plt.plot(kategori, deger, marker="o", linestyle="-", color="green")
            plt.title("Line Grafiği")

        elif grafik_tipi == "pie":
            if not pd.api.types.is_numeric_dtype(deger):
                return "❌ Pie grafik için değerler sayısal olmalı."
            plt.pie(deger, labels=kategori, autopct='%1.1f%%')
            plt.title("Pie Grafiği")

        else:
            return "❌ Desteklenmeyen grafik tipi. Kullan: bar, line, pie"

        plt.tight_layout()
        plt.savefig("grafik.png")
        plt.close()

        return "✅ Grafik oluşturuldu: grafik.png"

    except Exception as e:
        return f"⚠️ Grafik oluşturulamadı: {str(e)}"