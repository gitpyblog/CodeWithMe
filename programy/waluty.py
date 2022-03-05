import requests

# jaka_waluta = input('Jaka walutę chcesz sprawdzić? ')
# kurs_waluty = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/c/{jaka_waluta}/?format=json').json()
#
# ask = kurs_waluty['rates'][0]['ask']
# bid = kurs_waluty['rates'][0]['bid']

# print(f'\nOdpowiedź z API https://api.nbp.pl/api/exchangerates/rates/c/usd/?format=json:\n{kurs_waluty}\n')
# print(f"Aktualny kurs {kurs_waluty['currency']} na dzień {kurs_waluty['rates'][0]['effectiveDate']}:")
# print(f"Sprzedaż: {ask} zł")
# print(f"Skup: {bid} zł")

# http://api.nbp.pl/api/cenyzlota/?format=json

# kurs_zlota = requests.get('http://api.nbp.pl/api/cenyzlota/?format=json').json()


# print(f'answer{kurs_zlota}')
# print(kurs_zlota_uncja)

# Zadanie 1:
# Zaokrągli kotwę podsumowania portfela do 2 cyfr po przecinku
# print(round('portfel', 2))

# Zadanie 2:
# Zmieniono strukturę słownika z danymi portfela na następującą:


#dostosuj program do nowej struktury
# Iwona = {
#    'pln': 10000,
 #   'usd': 3000,
  #  'chf': 1000,
  #  'eur': 5000,
   # 'au': 5
# }

#Zadanie 3:
#Dodaj wyświetlanie danych dla więcej niż jednego portfela:

#Portfel = {
#   'Iwona': {
#       'imie': 'Iwona',
#       'nazwisko': 'Langner',
#       'data_utworzenia_portfela': '04.03.2022',
#       'waluty': {
#           'pln': 10000,
#           'usd': 3000,
#          'chf': 1000,
#           'eur': 5000,},
#       'metale': {
#           'au': 5}
#   },

#####################################################
kurs_zlota_json = requests.get('http://api.nbp.pl/api/cenyzlota/?format=json').json()
kurs_zlota_uncja = kurs_zlota_json[0]['cena'] * 32.1

kurs_dolara_json = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/c/usd/?format=json').json()
kurs_dolara = kurs_dolara_json['rates'][0]['bid']

kurs_euro_json = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/c/eur/?format=json').json()
kurs_euro = kurs_euro_json['rates'][0]['bid']

kurs_frank_json = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/c/chf/?format=json').json()
kurs_frank = kurs_frank_json['rates'][0]['bid']

Iwona = {
   'imie': 'Iwona',
    'nazwisko': 'Langner',
    'data_utworzenia_portfela': '04.03.2022',
    'waluty': {
        'pln': 10000,
        'usd': 3000,
        'chf': 1000,
        'eur': 5000,},
    'metale': {
       'au': 5}
}

portfel_Iwony = (Iwona['waluty']['usd'] * kurs_dolara) +\
          (Iwona['waluty']['chf'] * kurs_frank) +\
          (Iwona['waluty']['eur'] * kurs_euro) +\
          (Iwona['metale']['au'] * kurs_zlota_uncja)\
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
portfel_Dawida = (Dawid['waluty']['usd'] * kurs_dolara) +\
+ Dawid['waluty']['pln']
(Dawid['metale']['au'] * kurs_zlota_uncja)\

print(f'Łączna wartość w złotych portfela Iwony na dzień dzisiejszy to: {portfel_Iwony} zł')
print(round(portfel_Iwony, 2))  # zad. 1
print(f'Łączna wartość w złotych portfela Dawida na dzień dzisiejszy to: {portfel_Dawida} zł')
print(round(portfel_Dawida, 2))

