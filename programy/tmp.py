import requests


class Waluta:
    def __init__(self, code):
        """
        Klasa sprawdza aktualny kurs waluty z nbp.pl

        Args:
            code (str): trzyliterowy kod waluty.
        """
        waluta = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/c/{code}/?format=json').json()
        self.nazwa = waluta['currency']
        self.data = waluta['rates'][0]['effectiveDate']
        self.kup = waluta['rates'][0]['bid']
        self.sprzedaj = waluta['rates'][0]['ask']


usd = Waluta('usd')
chf = Waluta('chf')
eur = Waluta('eur')
kurs_au = requests.get('https://api.nbp.pl/api/cenyzlota/?format=json').json()
kurs_au = kurs_au[0]['cena'] * 31.1034  # Uncja trojańska

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

portfel = (Portfel['Iwona']['waluty']['usd'] * usd.sprzedaj) + \
          (Portfel['Iwona']['waluty']['chf'] * chf.sprzedaj) + \
          (Portfel['Iwona']['waluty']['eur'] * eur.sprzedaj) + \
          (Portfel['Iwona']['metale']['au'] * kurs_au) \
          + Portfel['Iwona']['waluty']['pln']

print(f"{Portfel['Iwona']['imie']} łączna wartość Twojego portfela na dzień dzisiejszy to: {round(portfel, 2)} zł")

print('W portfelu:')
print()
