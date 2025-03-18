class MusteriDestek:
    def __init__(self):
        self.sikayetler = []
    
    def sikayet_ekle(self, sikayet):
        self.sikayetler.append(sikayet)
    
    def listele(self):
        return self.sikayetler


class ReyonBakimi:
    def __init__(self):
        self.kontrol_listesi = []
    
    def ekle(self, urun):
        self.kontrol_listesi.append(urun)
    
    def listele(self):
        return self.kontrol_listesi


class StokIslemleri:
    def __init__(self):
        self.stok = {}
    
    def ekle(self, urun, miktar):
        self.stok[urun] = self.stok.get(urun, 0) + miktar
    
    def cikar(self, urun, miktar):
        if urun in self.stok and self.stok[urun] >= miktar:
            self.stok[urun] -= miktar
        else:
            print("Yetersiz stok!")
    
    def listele(self):
        return self.stok


class NobetCizelgesi:
    def __init__(self):
        self.nobet_listesi = {}
    
    def ekle(self, personel, tarih):
        self.nobet_listesi[tarih] = personel
    
    def listele(self):
        return self.nobet_listesi


class Izinler:
    def __init__(self):
        self.izin_listesi = {}
    
    def izin_ekle(self, personel, tarih):
        self.izin_listesi[tarih] = personel
    
    def listele(self):
        return self.izin_listesi


class MaasTablosu:
    def __init__(self):
        self.maaslar = {}
    
    def ekle(self, personel, maas):
        self.maaslar[personel] = maas
    
    def listele(self):
        return self.maaslar



