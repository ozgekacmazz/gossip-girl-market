import random


class JetKasa:
    def __init__(self):
        """Ürünleri ve satışları listelerde saklar."""
        self.urunler = []  # Ürünleri saklayacak liste
        self.satislar = []  # Satışları saklayacak liste

    def urun_ekle(self, isim, barkod, fiyat, kg_bazli):
        """Yeni ürün ekler."""
        urun = {"isim": isim, "barkod": barkod, "fiyat": fiyat, "kg_bazli": kg_bazli}
        self.urunler.append(urun)
        print(f"Ürün eklendi: {isim}")

    def urun_oku(self, barkod, kilo=None):
        """Ürünü barkod ile bul ve fiyatını hesapla."""
        for urun in self.urunler:
            if urun["barkod"] == barkod:
                fiyat = urun["fiyat"] * kilo if urun["kg_bazli"] and kilo else urun["fiyat"]
                return {"isim": urun["isim"], "toplam_fiyat": fiyat}
        return "Ürün bulunamadı!"

    def odeme_yap(self, tutar, odeme_tipi):
        """Nakit, kart veya RFID ile ödeme yap."""
        if odeme_tipi not in ["nakit", "kart", "rfid"]:
            return "Geçersiz ödeme yöntemi!"

        islem_no = random.randint(1000, 9999)
        self.satislar.append({"tutar": tutar, "odeme_tipi": odeme_tipi, "islem_no": islem_no})
        return f"Ödeme başarılı! {odeme_tipi.upper()} ile {tutar} TL ödendi. İşlem No: {islem_no}"

    def iade_yap(self, islem_no):
        """Satış işlemini iptal eder."""
        for satis in self.satislar:
            if satis["islem_no"] == islem_no:
                self.satislar.remove(satis)
                return f"İade işlemi başarılı! İşlem No: {islem_no} iptal edildi."
        return "İşlem bulunamadı!"


# === KULLANIM ÖRNEĞİ ===
jet_kasa = JetKasa()

# Ürün ekleyelim
jet_kasa.urun_ekle("Elma", "123456", 30, True)  # KG Bazlı ürün
jet_kasa.urun_ekle("Süt", "789101", 25, False)  # Adet Bazlı ürün

# Ürün okutalım (Barkod ile)
urun = jet_kasa.urun_oku("123456", kilo=2)  # 2 KG Elma
print(urun)

# Ödeme yapalım
if urun:
    print(jet_kasa.odeme_yap(urun['toplam_fiyat'], "kart"))

# İade işlemi yapalım
print(jet_kasa.iade_yap(1001))  # 1001 yerine gerçek işlem numarası girilmeli
