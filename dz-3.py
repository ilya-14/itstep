class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number  # Номер рахунку
        self.balance = balance  # Баланс рахунку

    def deposit(self, amount):
        """Метод для внесення грошей на рахунок."""
        if amount > 0:
            self.balance += amount
            print(f"Депозит успішний! Ваш новий баланс: {self.balance}")
        else:
            print("Сума для депозиту повинна бути більшою за нуль.")

    def withdraw(self, amount):
        """Метод для зняття грошей з рахунку."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Зняття успішне! Ваш новий баланс: {self.balance}")
            else:
                print("Недостатньо коштів на рахунку!")
        else:
            print("Сума для зняття повинна бути більшою за нуль.")

    def get_balance(self):
        """Метод для отримання поточного балансу."""
        return self.balance

account = BankAccount("UA123456789", 1000)  # Створюємо рахунок з номером і початковим балансом 1000

print(f"Баланс рахунку {account.account_number}: {account.get_balance()}")

account.deposit(500)  # Депозит на суму 500
account.withdraw(200)  # Зняття 200
account.withdraw(1500)  # Намагання зняти більше, ніж на рахунку
