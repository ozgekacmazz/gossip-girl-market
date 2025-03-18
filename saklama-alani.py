class SaklamaAlani:
    def __init__(self):
        """Saklama alanı verilerini liste olarak saklar."""
        self.veriler = []  # Tüm verileri saklayacak liste

    def veri_ekle(self, sicaklik, nem, doluluk):
        """Yeni sıcaklık, nem ve doluluk verisi ekler."""
        durum = self.durum_kontrol(sicaklik, nem, doluluk)
        veri = {"Sıcaklık": sicaklik, "Nem": nem, "Doluluk": doluluk, "Durum": durum}
        self.veriler.append(veri)
        print(f"Veri eklendi: {veri}")

    def durum_kontrol(self, sicaklik, nem, doluluk):
        """Sıcaklık, nem ve doluluk oranına göre durum belirler."""
        if sicaklik > 25:
            return "UYARI: Aşırı sıcak!"
        if nem > 70:
            return "UYARI: Aşırı nem!"
        if doluluk > 90:
            return "UYARI: Fazla doluluk!"
        return "Güvenli"

    def son_veri(self):
        """En son eklenen veriyi gösterir."""
        if self.veriler:
            return self.veriler[-1]
        return "Henüz veri yok."

# === KULLANIM ÖRNEĞİ ===
saklama = SaklamaAlani()

# Manuel veri ekleyelim
saklama.veri_ekle(22, 55, 70)
saklama.veri_ekle(28, 60, 80)  # Aşırı sıcak uyarısı alacak

# Son veriyi çekelim
print("Son veri:", saklama.son_veri())
