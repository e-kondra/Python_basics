import utils

currency = input("Enter a short-name of currency: ")
date, rate = utils.currency_rates(currency)
print(f'{rate} {date.isoformat()}')
