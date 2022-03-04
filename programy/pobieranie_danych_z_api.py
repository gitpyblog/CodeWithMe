import requests

jaka_waluta = input('Jaka walutę chcesz sprawdzić? ')
kurs_waluty = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/c/{jaka_waluta}/?format=json').json()

ask = kurs_waluty['rates'][0]['ask']
bid = kurs_waluty['rates'][0]['bid']

print(f'\nOdpowiedź z API https://api.nbp.pl/api/exchangerates/rates/c/usd/?format=json:\n{kurs_waluty}\n')
print(f"Aktualny kurs {kurs_waluty['currency']} na dzień {kurs_waluty['rates'][0]['effectiveDate']}:")
print(f"Sprzedaż: {ask} zł")
print(f"Skup: {bid} zł")
