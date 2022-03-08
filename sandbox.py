import requests

# TODO: rozszerzyć funkcjonalność o buy and sell
# TODO: przechowywanie portfeli w osobnym pliku
# TODO: obsługa innych metali

kurs_au_json = requests.get('https://api.nbp.pl/api/cenyzlota/?format=json').json()
kurs_au_uncja = kurs_au_json[0]['cena'] * 32.1


def aktualny_kurs(waluta, typ):
    kurs_waluty = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/c/{waluta}/?format=json').json()
    return kurs_waluty['rates'][0][typ]


Iwona = {
    'imie': 'Iwona',
    'nazwisko': 'Langner',
    'data_utworzenia_portfela': '04.03.2022',
    'waluty': {
        'pln': 10000,
        'usd': 3000,
        'chf': 1000,
        'eur': 5000, },
    'metale': {
        'au': 5}
}

portfel_Iwony = (Iwona['waluty']['usd'] * aktualny_kurs('usd', 'bid')) + \
                (Iwona['waluty']['chf'] * aktualny_kurs('chf', 'bid')) + \
                (Iwona['waluty']['eur'] * aktualny_kurs('eur', 'bid')) + \
                (Iwona['metale']['au'] * kurs_au_uncja) \
                + Iwona['waluty']['pln']

Dawid = {
    'imie': 'Dawid',
    'nazwisko': 'Szatkowski',
    'data_utworzenia_portfela': '05.03.2022',
    'waluty': {
        'pln': 0,
        'usd': 5000},
    'metale': {
        'au': 20}
}

portfel_Dawida = (Dawid['waluty']['usd'] * aktualny_kurs('usd', 'bid')) + \
                 + Dawid['waluty']['pln'] + \
                 (Dawid['metale']['au'] * kurs_au_uncja)

print(f'Łączna wartość w złotych portfela Iwony na dzień dzisiejszy to: {portfel_Iwony} zł')
print(round(portfel_Iwony, 2))  # zad. 1
print(f'Łączna wartość w złotych portfela Dawida na dzień dzisiejszy to: {portfel_Dawida} zł')
print(round(portfel_Dawida, 2))
