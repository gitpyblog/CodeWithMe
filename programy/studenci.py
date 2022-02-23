class Color:
    """ Klasa kolorująca tekst """
    GREEN = '\033[92m'  # GREEN
    RED = '\033[91m'  # RED
    YELLOW = '\033[93m'  # YELLOW
    LIGHTGREY = '\033[37m'
    BOLD = '\033[1m'  # POGRUBIENIE
    RESET = '\033[0m'  # RESET COLOR

def student(imie, nazwisko, semestr, *wykaz_przedmiotow, stypendium=False):
    def sprawdz_stypendium(status):
        if status is True:
            return f'{Color.GREEN}Przyznane{Color.RESET}'
        else:
            return f'{Color.RED}Nieprzyznane{Color.RESET}'

    return (
        f'🟢 {imie} {nazwisko}, '
        f'student {semestr} semestru, '
        f'wykaz przedmiotów: {", ".join(wykaz_przedmiotow)}. '
        f'{Color.LIGHTGREY}{Color.BOLD}Stypendium:{Color.RESET} {sprawdz_stypendium(stypendium)}')


janek = student('Janek', 'Kowalski', 2, 'matematyka', 'fizyka', 'biologia', 'chemia')
iwona = student('Iwona', 'Kowalska', 3, 'zarządzanie', 'python', 'filozofia', stypendium=True)
dawid = student('Dawid', 'Kowalski', 3, 'python', 'sql', 'matematyka')
zofia = student('Zosia', 'Tolar', 4, 'historia', 'j. angielski', 'filozofia')

print(f'\n{janek}\n{iwona}\n{dawid}\n{zofia}')
