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
    LIGHTGREY = '\033[37m'
    BOLD = '\033[1m'  # POGRUBIENIE
    RESET = '\033[0m'  # RESET COLOR


while True:
    ja = input('\nWybierz kamień, papier lub nożyce: ')
    lista = ('kamień', 'papier', 'nożyce')
    komputer = choice(lista)
    win = ('REMIS', 'WYGRAŁEŚ', 'PRZEGRAŁEŚ')

    if ja == komputer:
        print(f'{Mark.YELLOW}{win[0]}{Mark.LIGHTGREY} ({ja} vs {komputer}{Mark.RESET})')
    elif ja == 'kamień' and komputer == 'papier':
        print(f'{Mark.RED}{win[2]}{Mark.LIGHTGREY} ({ja} vs {komputer}{Mark.RESET})')
    elif ja == 'kamień' and komputer == 'nożyce':
        print(f'{Mark.GREEN}{win[1]}{Mark.LIGHTGREY} ({ja} vs {komputer}{Mark.RESET})')
    elif ja == 'papier' and komputer == 'nożyce':
        print(f'{Mark.RED}{win[2]}{Mark.LIGHTGREY} ({ja} vs {komputer}{Mark.RESET})')
    elif ja == 'papier' and komputer == 'kamień':
        print(f'{Mark.GREEN}{win[1]}{Mark.LIGHTGREY} ({ja} vs {komputer}{Mark.RESET})')
    elif ja == 'nożyce' and komputer == 'kamień':
        print(f'{Mark.RED}{win[2]}{Mark.LIGHTGREY} ({ja} vs {komputer}{Mark.RESET})')
    elif ja == 'nożyce' and komputer == 'papier':
        print(f'{Mark.GREEN}{win[1]}{Mark.LIGHTGREY} ({ja} vs {komputer}{Mark.RESET})')
    elif ja == 'koniec':
        print(f'{Mark.BOLD}Koniec gry{Mark.RESET}')
        break
    else:
        print(
            f"{Mark.LIGHTGREY}Wpisz: paper/kamień/nożyce lub koniec aby zakończyć{Mark.RESET}")
