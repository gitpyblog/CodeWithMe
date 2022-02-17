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
    you = input('\nWybierz kamień, papier lub nożyce: ')
    computer = choice(('kamień', 'papier', 'nożyce'))
    winner = ('REMIS', 'WYGRAŁEŚ', 'PRZEGRAŁEŚ')

    if you == computer:
        print(f'{Mark.YELLOW}{winner[0]}{Mark.LIGHTGREY} ({you} vs {computer}{Mark.RESET})')
    elif you == 'kamień' and computer == 'papier':
        print(f'{Mark.RED}{winner[2]}{Mark.LIGHTGREY} ({you} vs {computer}{Mark.RESET})')
    elif you == 'kamień' and computer == 'nożyce':
        print(f'{Mark.GREEN}{winner[1]}{Mark.LIGHTGREY} ({you} vs {computer}{Mark.RESET})')
    elif you == 'papier' and computer == 'nożyce':
        print(f'{Mark.RED}{winner[2]}{Mark.LIGHTGREY} ({you} vs {computer}{Mark.RESET})')
    elif you == 'papier' and computer == 'kamień':
        print(f'{Mark.GREEN}{winner[1]}{Mark.LIGHTGREY} ({you} vs {computer}{Mark.RESET})')
    elif you == 'nożyce' and computer == 'kamień':
        print(f'{Mark.RED}{winner[2]}{Mark.LIGHTGREY} ({you} vs {computer}{Mark.RESET})')
    elif you == 'nożyce' and computer == 'papier':
        print(f'{Mark.GREEN}{winner[1]}{Mark.LIGHTGREY} ({you} vs {computer}{Mark.RESET})')
    elif you == 'koniec':
        print(f'{Mark.BOLD}Koniec gry{Mark.RESET}')
        break
    else:
        print(f"{Mark.LIGHTGREY}Wpisz: paper/kamień/nożyce lub koniec aby zakończyć{Mark.RESET}")
