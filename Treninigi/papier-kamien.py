# podajesz w terminalu kamień, papier, nożyce
# komputer losuje swoje zagranie
# Komputer porównuje Twoje ze swoim
# Wyświetla wynik rundy
# gra zaczyna się od nowa
from random import choice


class Mark:
    """ Klasa kolorująca tekst """
    GREEN = '\033[92m'  # GREEN
    RED = '\033[91m'  # RED
    YELLOW = '\033[93m'  # YELLOW
    RESET = '\033[0m'  # RESET COLOR


while True:
    ja = input('Wybierz kamień, papier lub nożyce: ')
    lista = ('kamień', 'papier', 'nożyce', 'koniec gry')
    komputer = choice(lista)
    win = ('remis', 'wygrałeś', 'przegrałeś')

    if ja == komputer:
        print(f'{Mark.YELLOW}{win[0]}{Mark.RESET} - komputer wylosował: {komputer}')
    if ja == 'kamień' and komputer == 'papier':
        print(f'{Mark.RED}{win[2]}{Mark.RESET} - komputer wylosował: {komputer}')
    if ja == 'kamień' and komputer == 'nożyce':
        print(f'{Mark.GREEN}{win[1]}{Mark.RESET} - komputer wylosował: {komputer}')
    if ja == 'papier' and komputer == 'nożyce':
        print(f'{Mark.RED}{win[2]}{Mark.RESET} - komputer wylosował: {komputer}')
    if ja == 'papier' and komputer == 'kamień':
        print(f'{Mark.GREEN}{win[1]}{Mark.RESET} - komputer wylosował: {komputer}')
    if ja == 'nożyce' and komputer == 'kamień':
        print(f'{Mark.RED}{win[2]}{Mark.RESET} - komputer wylosował: {komputer}')
    if ja == 'nożyce' and komputer == 'papier':
        print(f'{Mark.GREEN}{win[1]}{Mark.RESET} - komputer wylosował: {komputer}')
    if ja not in lista:
        print('wybierz: paper, kamień, nożyce, lub wybierz koniec gry')
    if ja == 'koniec gry':
        print('koniec gry')
        break

