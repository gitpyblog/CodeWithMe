def is_even(number: int) -> bool:
    """
    Funkcja sprawdza, czy podana liczba jest parzysta

    Args:
        number (int | float): liczba, którą weryfikujemy

    Returns:
        bool: zwraca True, jeśli liczba jest parzysta
    """

    if type(number) is not int:
        raise TypeError("Niepoprawna liczba")

    return True if number % 2 == 0 else False


print(is_even(5))

# pystrat.pl
# pycamp.pl
