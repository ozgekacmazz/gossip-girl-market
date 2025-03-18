
import sqlite3
import random
import time

class SaklamaAlani:
    def __init__(self, db_path="market.db"):
        """Veritabanı bağlantısını başlatır."""
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Saklama alanı verilerini kaydetmek için tablo oluşturur."""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS storage (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperature REAL,
            humidity REAL,
            occupancy REAL,
            status TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)
        self.conn.commit()

    def add_storage_data(self, temperature, humidity, occupancy):
        """Sıcaklık, nem ve doluluk verilerini kaydeder."""
        status = self.check_status(temperature, humidity, occupancy)
        self.cursor.execute("INSERT INTO storage (temperature, humidity, occupancy, status) VALUES (?, ?, ?, ?)",
                            (temperature, humidity, occupancy, status))
        self.conn.commit()
        return f"Veri kaydedildi -> Sıcaklık: {temperature}°C, Nem: {humidity}%, Doluluk: {occupancy}%, Durum: {status}"

    def check_status(self, temperature, humidity, occupancy):
        """Saklama alanının güvenli olup olmadığını kontrol eder."""
        if temperature > 25:
            return "UYARI: Aşırı sıcak!"
        elif humidity > 70:
            return "UYARI: Aşırı nem!"
        elif occupancy > 90:
            return "UYARI: Fazla doluluk!"
        else:
            return "Güvenli"

    def get_latest_data(self):
        """Son kaydedilen saklama alanı verisini getirir."""
        self.cursor.execute("SELECT * FROM storage ORDER BY timestamp DESC LIMIT 1")
        return self.cursor.fetchone()

    def simulate_sensor(self):
        """Rastgele sensör verileri üretir ve kaydeder (Gerçek zamanlı takip için kullanılabilir)."""
        while True:
            temp = random.uniform(15, 30)  # Sıcaklık 15-30°C arasında
            humidity = random.uniform(40, 80)  # Nem 40-80% arasında
            occupancy = random.uniform(50, 100)  # Doluluk oranı %50-100 arasında

            print(self.add_storage_data(temp, humidity, occupancy))
            time.sleep(5)  # 5 saniyede bir veri üret

# === KULLANIM ÖRNEĞİ ===
saklama = SaklamaAlani()

# Manuel veri ekleme
print(saklama.add_storage_data(22, 55, 70))

# Son veriyi çekme
print("Son veri:", saklama.get_latest_data())

# Gerçek zamanlı sensör simülasyonu başlat (İstersen yorumdan çıkar)
# saklama.simulate_sensor()
