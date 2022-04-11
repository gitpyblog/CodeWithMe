def student(imie:str, nazwisko:str, semestr:int, *przedmioty, stypendium=False):
    def weryfikuj_stypendium(status):
        if status is True:
            return '\033[92m'+'Przyznane'+'\033[0m'
        else:
            return '\033[91m'+'Nieprzyznane'+'\033[0m'

    return (
        f'🟢 {imie} {nazwisko}, '
        f'student {semestr} semestru, '
        f'wykaz przedmiotów: {", ".join(przedmioty)}. '
        f'Stypendium: {weryfikuj_stypendium(stypendium)}')



janek = student('Janek', 'Kowalski', 2, 'matematyka', 'fizyka', 'biologia', 'chemia')
iwona = student('Iwona', 'Kowalska', 3, 'zarządzanie', 'python', 'filozofia', stypendium=True)
dawid = student('Dawid', 'Kowalski', 3, 'matematyka', 'algorytmika', 'logika')
zofia = student('Zosia', 'Tolar', 4, 'historia', 'j. angielski', 'filozofia')



print(f'\n{janek}\n{iwona}\n{dawid}\n{zofia}')
