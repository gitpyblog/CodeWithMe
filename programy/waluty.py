import json
import requests

response_get = requests.get('https://api.nbp.pl/api/exchangerates/rates/c/usd/?format=json')
response_json = json.loads(response_get.text)
print(f'\nOdpowiedź z https://api.nbp.pl/api/exchangerates/rates/c/usd/?format=json:\n{response_json}\n')

ask = response_json['rates'][0]['ask']
bid = response_json['rates'][0]['bid']

print(f"Aktualny kurs {response_json['currency']} na dzień {response_json['rates'][0]['effectiveDate']}:")
print(f"Sprzedaż: {ask} zł")
print(f"Skup: {bid} zł")
