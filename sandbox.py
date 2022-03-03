# http://api.nbp.pl/
# http://api.nbp.pl/api/exchangerates/rates/a/usd/
import requests

kurs_dolara = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/usd/')
print(kurs_dolara.text)

result = kurs_dolara.text.split(',')
result = result[5]
print(f' Aktualny kurs dolara: {result[6:12]}')

zl = input('Ile dolarów chcesz sprzedać ')
dolar = float(result[6:12]) * float(zl)

print(f' Otrzymałeś: {dolar}zł (Wymieniłeś {zl}$)')
