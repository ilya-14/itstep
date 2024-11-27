class ConverterValut:
    def __init__(self):
        self.exchange_rates = {
            'UAH': 41.5035,
            'EUR': 1.06,
            'JPY': 2.7076
        }

    def add_exchange_rate(self, currency, rate):
        self.exchange_rates[currency] = rate

    def convert_to_usd(self, currency, amount):
        if currency in self.exchange_rates:
            return amount * self.exchange_rates[currency]
        else:
            return None

converter = ConverterValut()

currency = input("Введіть валюту (UAH, EUR, JPY): ").upper()

if currency in converter.exchange_rates:
    amount = float(input(f"Введіть кількість {currency}: "))
    usd_amount = converter.convert_to_usd(currency, amount)
    print(f"{amount} {currency} дорівнює {usd_amount} доларів США.")
else:
    print("Невідома валюта. Спробуйте ще раз.")
