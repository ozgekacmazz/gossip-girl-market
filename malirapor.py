from datetime import datetime, timedelta

# Gelir ve giderleri takip etmek için sözlükler
giderler = []

def add_expense(description, amount):
    giderler.append({"description": description, "amount": amount, "date": datetime.now().strftime("%Y-%m-%d")})
    print(f"{description} için {amount} TL harcama kaydedildi.")

def daily_expense_report():
    today = datetime.now().strftime("%Y-%m-%d")
    total = sum(exp["amount"] for exp in giderler if exp["date"] == today)
    print(f"Bugünkü toplam gider: {total} TL")

def weekly_expense_report():
    week_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    total = sum(exp["amount"] for exp in giderler if exp["date"] >= week_ago)
    print(f"Son 7 gündeki toplam gider: {total} TL")

# Kullanım
while True:
    print("1. Gider Ekle")
    print("2. Günlük Gider Raporu")
    print("3. Haftalık Gider Raporu")
    print("4. Çıkış")
    
    choice = input("Seçiminizi yapın: ")
    
    if choice == "1":
        description = input("Gider açıklaması: ")
        amount = float(input("Tutar: "))
        add_expense(description, amount)
    elif choice == "2":
        daily_expense_report()
    elif choice == "3":
        weekly_expense_report()
    elif choice == "4":
        break
    else:
        print("Geçersiz seçim!")
