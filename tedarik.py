class Urun:
    def __init__(self, isim, stok_miktari, kritik_seviye):
        self.isim = isim
        self.stok_miktari = stok_miktari
        self.kritik_seviye = kritik_seviye

    def stok_guncelle(self, miktar):
        self.stok_miktari -= miktar
        print(f"{miktar} {self.isim} satıldı. Kalan stok: {self.stok_miktari}")
        self.stok_kontrol()

    def stok_kontrol(self):
        if self.stok_miktari <= self.kritik_seviye:
            print(f"⚠️  {self.isim} stok kritik seviyede! (Kalan: {self.stok_miktari}) - Sipariş ver!")
        else:
            print(f"✅  {self.isim} stok yeterli. (Kalan: {self.stok_miktari})")


urunler = [
    Urun("Ekler", stok_miktari=20, kritik_seviye=5),
    Urun("Baklava", stok_miktari=50, kritik_seviye=10),
    Urun("Poğaça", stok_miktari=30, kritik_seviye=7)
]

def satis_yap(urun_adi, miktar):
    for urun in urunler:
        if urun.isim.lower() == urun_adi.lower():
            urun.stok_guncelle(miktar)
            return
    print(f"{urun_adi} bulunamadı.")
