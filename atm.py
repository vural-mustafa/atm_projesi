class ATM:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"{amount} TL çekildi. Yeni bakiye: {self.balance} TL"
        else:
            return "İşlem başarısız. Yetersiz bakiye."

    def deposit(self, amount):
        self.balance += amount
        return f"{amount} TL yatırıldı. Yeni bakiye: {self.balance} TL"

    def transfer(self, tc, iban, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"{amount} TL, {tc} TC kimlik numarasına ait {iban} IBAN numarasına havale edildi. Yeni bakiye: {self.balance} TL"
        else:
            return "İşlem başarısız. Yetersiz bakiye."

def main():
    initial_balance = 1000  # Başlangıç bakiyesi
    atm = ATM(initial_balance)

    while True:
        print("\n1-Para Çekme\n2-Para Yatırma\n3-Havale Yapma\n4-Çıkış Yap")
        choice = input("Lütfen yapmak istediğiniz işlemi seçin: ")

        if choice == '1':
            amount = float(input("Çekmek istediğiniz miktarı girin: "))
            print(atm.withdraw(amount))

        elif choice == '2':
            amount = float(input("Yatırmak istediğiniz miktarı girin: "))
            print(atm.deposit(amount))

        elif choice == '3':
            tc = input("Havale yapılacak kişinin TC kimlik numarasını girin: ")
            iban = input("Havale yapılacak kişinin IBAN numarasını girin: ")
            amount = float(input("Havale miktarını girin: "))
            print(atm.transfer(tc, iban, amount))

        elif choice == '4':
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
