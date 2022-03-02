# def funk(nazwisko, **kwargs):
#     print("Nazwisko:", nazwisko)
#     for key, item in kwargs.items():
#         print("Imię:", key, "Wiek:", item)
#
#
# funk("Kowalscy", Ewa=33, Michał=44, Adam=14, Ola=5)
from datetime import datetime

# people = {
#     'Ola': 5,
#     'Ewa': 33,
#     'Zosia': 27,
#     'Andrzej': 33,
#     'Iwona': 41}


# print(f"PATRZ TUTAJ:")


# def calculate_age(wiek):
#     now = datetime.now().year
#     for key, volue in wiek.items():
#         print(f'imię: {key}, wiek: {volue}')
#
#
# calculate_age(people)
#
#
# def calculate_age2(**wiek):
#     now = datetime.now().year
#     for key, volue in wiek.items():
#         print(f'imię: {key}, wiek: {volue}')
#
#
# calculate_age2(Adam=33, Ola=15)

#     print("Imię:", key, "Wiek:", item)


# wiek = int(input('podaj swoj wiek: '))
# print(calculate_age(wiek))

# for key, item in people.items():
#     print("Imię:", key, "Wiek:", item)
#
# # x = 2
# # y = 5
#
# # x, y, z = 2, 5, 7
# # print(x)
# # print(y)
# # print(z)
#
# krotka = (1, 2, 3, 5, 8)
#
# a, b, c, d, e = krotka
# print(c)


class Mark:
    """ Klasa kolorująca tekst """
    GREEN = '\033[92m'  # GREEN
    YELLOW = '\033[93m'  # YELLOW
    RED = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR

print(f'{Mark.RED}Ala m{Mark.RESET}a {Mark.GREEN}kota{Mark.RESET}')