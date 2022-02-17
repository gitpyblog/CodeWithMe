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
    you: str = input('\nWybierz kamień, papier lub nożyce: ')
    computer: str = choice(('kamień', 'papier', 'nożyce'))
    winner = (f'{Mark.YELLOW}REMIS{Mark.RESET} {Mark.LIGHTGREY}({you} vs {computer}{Mark.RESET})',
              f'{Mark.GREEN}WYGRAŁEŚ{Mark.RESET} {Mark.LIGHTGREY}({you} vs {computer}{Mark.RESET})',
              f'{Mark.RED}PRZEGRAŁEŚ{Mark.RESET} {Mark.LIGHTGREY}({you} vs {computer}{Mark.RESET})')

    if you == computer:
        print(f'{winner[0]}')
    elif you == 'nożyce' and computer == 'papier':
        print(f'{winner[1]}')
    elif you == 'kamień' and computer == 'nożyce':
        print(f'{winner[1]}')
    elif you == 'papier' and computer == 'kamień':
        print(f'{winner[1]}')
    elif you == 'kamień' and computer == 'papier':
        print(f'{winner[2]}')
    elif you == 'papier' and computer == 'nożyce':
        print(f'{winner[2]}')
    elif you == 'nożyce' and computer == 'kamień':
        print(f'{winner[2]}')
    elif you == 'koniec':
        print(f'{Mark.BOLD}Koniec gry{Mark.RESET}')
        break
    else:
        print(f"{Mark.LIGHTGREY}Wpisz: 'paper', 'kamień', 'nożyce' lub 'koniec' aby zakończyć grę.{Mark.RESET}")
