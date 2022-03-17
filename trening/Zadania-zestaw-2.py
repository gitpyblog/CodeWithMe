# Napisz funckję sprawdzającą, czy podana liczba jest parzysta
pass

# Napisz dokumentację do powyższej funkcji sprawdzającej parzystość liczby
pass

# Napisz funkcję, która przyjemnie dowolną ilość argumentów następnie je wszystkie wyświetli
def argumenty(*args):
    for element in args:
        print(element)


# Napisz funkcję, który oblicza pole i obwód koła o promieniu podanym przez użytkownika.
# Wartość stałej PI weź z biblioteki math. Promień nie może być ujemny.
# W przypadku podania liczby ujemnej program powinien wyświetlić komunikat o błędzie.
def circle(r):
    """
    Args:
        r: User podaje dł. promienia, który przyjmuje f'

    Returns:
        zwraca pole koła i obwód koła
    """
    import math  # https://docs.python.org/3/library/math.html
    pi = math.pi
    if r <= 0:
        print('prominent nie more byc liczbą ujemną: ')
    else:
        print('Pole koła: ', pi * r ** 2)
        print('Obwód koła: ', 2 * pi * r)


# Napisz program, który wylosuję liczbę od 1 do 100, a następnie będzie prosił użytkownika o jej odgadnięcie tak długo aż mu się to uda.
# Program powinien informować użytkownika czy podana przez niego propozycja jest mniejsza, czy większa od zgadywanej.
pass

# Napisz funkcję, która ponumeruje wszystkie znaki w podanym przez użytkownika stringu, a następnie wyświetli numeracje
def numeruj(tekst: str):
    for index, litera in enumerate(tekst, start=1):
        print(f'{index} - {litera}')


# utwórz wektor a = e + f + e * f - e**2, gdzie:
# współrzędne wektora e to liczby nieparzyste od 1 do 2022 na przemian przemnożone przez 1 i -1
# współrzędne wektora f są pierwiastkami liczb parzystych od 2 do 2022
e = range(1, 2022, 2)
licznik_pozycji = 0
new_e = list()
for n in e:
    if licznik_pozycji == 0:
        new_e.append(n * 1)
        licznik_pozycji += 1
    else:
        new_e.append(n * -1)
        licznik_pozycji = 0
