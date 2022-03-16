import requests
from coloratura import cprint, Pantone, Bit4

# print('KLUCZE:'
#       'id_stacji,'
#       'stacja,'
#       'data_pomiaru,'
#       'godzina_pomiaru,'
#       'temperatura,'
#       'predkosc_wiatru,'
#       'kierunek_wiatru,'
#       'wilgotnosc_wzgledna',
#       'suma_opadu,',
#       'cisnienie')

imgw = requests.get('https://danepubliczne.imgw.pl/api/data/synop').json()


def pogoda(miasto, czynnik):
    for i in imgw:
        if i['stacja'] == miasto:
            cprint(i['stacja'], color=Pantone.ILLUMINATING)

            if czynnik == 'tmp':
                temperatura = float(i['temperatura'])
                if temperatura <= -1:
                    cprint(i['temperatura'], color=Pantone.CLASSIC_BLUE)
                elif 0 <= temperatura >= 10:  # warunki brzegowe
                    cprint(i['temperatura'], color=Bit4.BLUE)
                elif 11 <= temperatura >= 20:
                    cprint(i['temperatura'], color=Pantone.ILLUMINATING)
                elif 21 <= temperatura >= 30:
                    cprint(i['temperatura'], color=Pantone.LIVING_CORAL)
                elif temperatura <= 31:
                    cprint(i['temperatura'], color=Bit4.RED)
                else:
                    print(i['temperatura'])


pogoda(input('Podaj nazwę miasta: '), input('Podaj nazwę klucza: '))
