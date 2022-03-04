import requests

kurs_au_json = requests.get('https://api.nbp.pl/api/cenyzlota/?format=json').json()
kurs_au_uncja = kurs_au_json[0]['cena'] * 32.1

kurs_dolara_json = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/c/usd/?format=json').json()
kurs_dolara = kurs_dolara_json['rates'][0]['bid']

kurs_euro_json = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/c/eur/?format=json').json()
kurs_euro = kurs_euro_json['rates'][0]['bid']

kurs_frank_json = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/c/chf/?format=json').json()
kurs_frank = kurs_frank_json['rates'][0]['bid']

Iwona = {
    'pln': 10000,
    'usd': 3000,
    'chf': 1000,
    'eur': 5000,
    'au': 5
}

portfel = (Iwona['usd'] * kurs_dolara) + \
          (Iwona['chf'] * kurs_frank) + \
          (Iwona['eur'] * kurs_euro) + \
          (Iwona['au'] * kurs_au_uncja) \
          + Iwona['pln']

print(f'Łączna wartość w złotych Twojego portfela na dzień dzisiejszy to: {portfel} zł')
