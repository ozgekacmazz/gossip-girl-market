class Urun:
    def __init__(self, isim, satis_tipi):
        self.isim = isim
        self.satis_tipi = satis_tipi

    def satin_al(self, miktar):
        if self.satis_tipi == 'adet':
            print(f"{miktar} adet {self.isim} hazırlandı.")
        elif self.satis_tipi == 'kilo':
            print(f"{miktar} kg {self.isim} tartıldı.")
        else:
            print("Geçersiz satış tipi!")


urunler = [
    Urun("Ekler", "adet"),
    Urun("Baklava", "kilo"),
    Urun("Poğaça", "adet"),
    Urun("Kuru Pasta", "kilo")
]

def reyon_yonlendirme(urun_adi, miktar):
    for urun in urunler:
        if urun.isim.lower() == urun_adi.lower():
            urun.satin_al(miktar)
            return
    print(f"{urun_adi} bulunamadı.")
