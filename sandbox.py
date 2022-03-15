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

            if czynnik == 'temperatura':
                if float(i['temperatura']) <= -1:
                    cprint(i['temperatura'], color=Pantone.CLASSIC_BLUE)
                elif 0 >= float(i['temperatura']) >= 10:  # warunki brzegowe
                    cprint(i['temperatura'], color=Bit4.BLUE)
                elif 11 >= float(i['temperatura']) >= 20:
                    cprint(i['temperatura'], color=Pantone.ILLUMINATING)
                elif 21 >= float(i['temperatura']) >= 30:
                    cprint(i['temperatura'], color=Pantone.LIVING_CORAL)
                elif 31 >= float(i['temperatura']):
                    cprint(i['temperatura'], color=Bit4.RED)


pogoda(input('Podaj nazwę miasta: '), input('Podaj nazwe klucza: '))
