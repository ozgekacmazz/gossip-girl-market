from datetime import datetime, timedelta

# Ürün stokları ve satışları takip etmek için sözlükler
urunler = {}
satislar = []

def add_product(name, stock, price):
    urunler[name] = {"stock": stock, "price": price}

def update_stock(name, quantity):
    if name in urunler:
        urunler[name]["stock"] += quantity
    else:
        print("Ürün bulunamadı.")

def record_sale(name, quantity):
    if name in urunler and urunler[name]["stock"] >= quantity:
        urunler[name]["stock"] -= quantity
        satislar.append({"name": name, "quantity": quantity, "date": datetime.now().strftime("%Y-%m-%d")})
        print(f"{quantity} adet {name} satıldı.")
    else:
        print("Yetersiz stok veya ürün bulunamadı.")

def daily_sales_report():
    today = datetime.now().strftime("%Y-%m-%d")
    report = {}
    for sale in satislar:
        if sale["date"] == today:
            report[sale["name"]] = report.get(sale["name"], 0) + sale["quantity"]
    print("Günlük Satış Raporu:")
    for name, quantity in report.items():
        print(f"{name}: {quantity} adet satıldı")

def weekly_sales_report():
    week_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    report = {}
    for sale in satislar:
        if sale["date"] >= week_ago:
            report[sale["name"]] = report.get(sale["name"], 0) + sale["quantity"]
    print("Haftalık Satış Raporu:")
    for name, quantity in report.items():
        print(f"{name}: {quantity} adet satıldı")

# Kullanım
add_product("Süt", 50, 25.0)
add_product("Ekmek", 100, 5.0)

while True:
    print("1. Ürün Ekle")
    print("2. Stok Güncelle")
    print("3. Satış Yap")
    print("4. Günlük Rapor")
    print("5. Haftalık Rapor")
    print("6. Çıkış")
    
    choice = input("Seçiminizi yapın: ")
    
    if choice == "1":
        name = input("Ürün adı: ")
        stock = int(input("Stok miktarı: "))
        price = float(input("Fiyat: "))
        add_product(name, stock, price)
    elif choice == "2":
        name = input("Ürün adı: ")
        quantity = int(input("Eklenen stok miktarı: "))
        update_stock(name, quantity)
    elif choice == "3":
        name = input("Satılacak ürün adı: ")
        quantity = int(input("Miktar: "))
        record_sale(name, quantity)
    elif choice == "4":
        daily_sales_report()
    elif choice == "5":
        weekly_sales_report()
    elif choice == "6":
        break
    else:
        print("Geçersiz seçim!")
