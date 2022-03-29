# Napisz funckję sprawdzającą, czy podana liczba jest parzysta
# Napisz dokumentację do tej funkcji
def czy_parzysta(x):
    """
    Args: funkcja przyjmuje dowolną liczbę
        x: dowolna liczba

    Returns: prawda, jeśli liczba jest parzysta
    """
    if x % 2 == 0:
        return True
    else:
        return False


print(czy_parzysta(7))


# Napisz funkcję, która przyjemnie dowolną ilość argumentów następnie je wszystkie wyświetli
def argumenty(*args):
    print(args)


argumenty(1, 2, 3, 'kot')


# Napisz funkcję, który oblicza pole i obwód koła o promieniu podanym przez użytkownika.
# W przypadku podania liczby ujemnej program powinien wyświetlić komunikat o błędzie.
def oblicz(r):
    if r <= 0:
        print('podałeś liczbę ujemną')
    else:
        print('pole koła', round(3.14 * r ** 2))
        print('obwód koła', round(2 * 3.14 * r, 2))


oblicz(5)


# Napisz funkcję, która ponumeruje wszystkie znaki w podanym przez użytkownika stringu, a następnie wyświetli numeracje
def numerowanie(x):
    for i, znak in enumerate(x.keys(), start=1):
        print(i, znak)


numerowanie({'a': 'kot', 'b': 'pies'})
