import requests

kurs_au_json = requests.get('https://api.nbp.pl/api/cenyzlota/?format=json').json()
kurs_au_uncja = kurs_au_json[0]['cena'] * 32.1

kurs_dolara_json = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/c/usd/?format=json').json()
kurs_dolara = kurs_dolara_json['rates'][0]['bid']

kurs_euro_json = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/c/eur/?format=json').json()
kurs_euro = kurs_euro_json['rates'][0]['bid']

kurs_frank_json = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/c/chf/?format=json').json()
kurs_frank = kurs_frank_json['rates'][0]['bid']

Portfel = {
    'Iwona': {
        'imie': 'Iwona',
        'nazwisko': 'Langner',
        'data_utworzenia_portfela': '04.03.2022',
        'waluty': {
            'pln': 10000,
            'usd': 3000,
            'chf': 1000,
            'eur': 5000},
        'metale': {
            'au': 5}
    },
    'Dawid': {
        'imie': 'Dawid',
        'nazwisko': 'Szatkowski',
        'data_utworzenia_portfela': '05.03.2022',
        'waluty': {
            'pln': 0,
            'usd': 5000},
        'metale': {
            'au': 20}
    }
}

portfel = (Portfel['Iwona']['waluty']['usd'] * kurs_dolara) + \
          (Portfel['Iwona']['waluty']['chf'] * kurs_frank) + \
          (Portfel['Iwona']['waluty']['eur'] * kurs_euro) + \
          (Portfel['Iwona']['metale']['au'] * kurs_au_uncja) \
          + Portfel['Iwona']['waluty']['pln']

print(f"{Portfel['Iwona']['imie']} łączna wartość w złotych Twojego portfela na dzień dzisiejszy to: {portfel} zł")
