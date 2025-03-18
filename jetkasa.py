import sqlite3
import random


class JetKasa:
    def __init__(self, db_path="market.db"):
        """Veri tabanı bağlantısını başlatır."""
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Ürün ve satış tablolarını oluşturur."""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            barcode TEXT UNIQUE,
            price REAL,
            weight_based INTEGER,  -- 1: Kilogram bazlı ürün, 0: Adet bazlı ürün
            stock REAL
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            quantity REAL,
            total_price REAL,
            payment_method TEXT,
            FOREIGN KEY(product_id) REFERENCES products(id)
        )
        """)
        self.conn.commit()

    def scan_product(self, barcode, weight=None):
        """Ürünü barkod veya RFID ile bul ve fiyatı hesapla."""
        self.cursor.execute("SELECT id, name, price, weight_based FROM products WHERE barcode=?", (barcode,))
        product = self.cursor.fetchone()

        if not product:
            return "Ürün bulunamadı!"

        product_id, name, price, weight_based = product

        if weight_based and weight:
            total_price = price * weight  # KG bazlı fiyat
        else:
            total_price = price  # Adet bazlı fiyat

        return {"id": product_id, "name": name, "total_price": total_price}

    def process_payment(self, total_amount, method):
        """Nakit veya kart ile ödeme işlemi yapar."""
        if method not in ["cash", "card", "rfid"]:
            return "Geçersiz ödeme yöntemi!"

        transaction_id = random.randint(1000, 9999)
        return f"Ödeme başarılı! {method.upper()} ile {total_amount} TL ödendi. İşlem No: {transaction_id}"

    def refund(self, sale_id):
        """Satış işleminden sonra iade yapar."""
        self.cursor.execute("DELETE FROM sales WHERE id=?", (sale_id,))
        self.conn.commit()
        return f"İade işlemi başarılı! İşlem No: {sale_id} iptal edildi."

    def add_product(self, name, barcode, price, weight_based, stock):
        """Yeni ürün ekler."""
        self.cursor.execute("INSERT INTO products (name, barcode, price, weight_based, stock) VALUES (?, ?, ?, ?, ?)",
                            (name, barcode, price, weight_based, stock))
        self.conn.commit()
        print(f"{name} ürünü eklendi!")


# === KULLANIM ÖRNEĞİ ===
jet_kasa = JetKasa()

# Yeni Ürünler Ekleyelim
jet_kasa.add_product("Elma", "123456", 30, 1, 100)  # KG Bazlı
jet_kasa.add_product("Süt", "789101", 25, 0, 50)  # Adet Bazlı

# Ürünü Okutalım (Barkod veya RFID)
urun = jet_kasa.scan_product("123456", weight=2)  # 2 KG Elma
print(urun)

# Ödeme İşlemi (Kart/Nakit)
if urun:
    print(jet_kasa.process_payment(urun['total_price'], "card"))

# İade İşlemi
print(jet_kasa.refund(1))

