import requests

response_json = requests.get('https://api.nbp.pl/api/exchangerates/rates/c/usd/?format=json').json()

ask = response_json['rates'][0]['ask']
bid = response_json['rates'][0]['bid']

print(f'\nOdpowiedź z API https://api.nbp.pl/api/exchangerates/rates/c/usd/?format=json:\n{response_json}\n')
print(f"Aktualny kurs {response_json['currency']} na dzień {response_json['rates'][0]['effectiveDate']}:")
print(f"Sprzedaż: {ask} zł")
print(f"Skup: {bid} zł")
