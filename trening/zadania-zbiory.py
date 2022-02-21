# Napisz program, który utworzy dwa # X oraz Y, zbiór X zawiera a elementów, zbiór Y zawiera b elementów.
# Wartości a oraz b to losowe liczby całkowite z przedziału <4,7>.
# Zbiory powinny zawierać elementy o losowej wartości z przedziału <0,10>.
# Następnie wykonaj następujące ćwiczenia:
# 1. Wypisz na ekran informację czy zbiór X zawiera liczbę 5.
# 2. Wypisz na ekran sumę zbiorów X oraz Y.
# 3. Wypisz na ekran różnicę zbiorów X oraz Y.
# 4. Wypisz na ekran różnicę zbiorów Y oraz X.
# 5. Wypisz na ekran wartość najwyższego elementu w obu zbiorach.
# 6. Usuń ze zbioru X pierwszy element i dołącz go do zbioru Y.
# 7. Przekopiuj wszystkie elementy zbioru X do zbioru Y.
# 8. Wypisz na ekran część wspólną zbiorów X oraz Y.


from random import sample, randint

import lista as lista

a = randint(4, 7)
b = randint(4, 7)
X = set(sample(range(10), a))  # sample określa ile razy ma powtarzać losowanie sample('przedział', ilość powtórzeń)
Y = set(sample(range(10), b))


def zad1(x):  # 1. Wypisz na ekran informację czy zbiór X zawiera liczbę 5.
    if 5 in x:
        return f'Zad1: 5 zwiera się w X: {X}'
    else:
        return f'Zad1: 5 nie zawiera się X: {X}'


def zad2(x, y):  # 2. Wypisz na ekran sumę zbiorów X oraz Y
    return f'Zad2: Suma zbiorów X i Y to: {sum(x.union(y))} {x.union(y)}'


def zad3(x, y):  # 3-4. Wypisz na ekran różnicę zbiorów X i Y oraz Y i X.
    return f'Zad3: Zad4: Różnica X-Y oraz Y-X: {x.symmetric_difference(y)}'


def zad5(x, y):  # 5. Wypisz na ekran wartość najwyższego elementu w obu zbiorach.
    lista_xy = x.symmetric_difference(y)
    return f'Zad5: Najwyższa wartość w obu zbiorach to {max(lista_xy)}'


def zad6(x, y):  # Usuń ze zbioru X pierwszy element i dołącz go do zbioru Y.
    new_list = list(x)
    new_list.remove(new_list[0])
    return 'Zad6: Zadanie nie możliwe do rozwiązania ponieważ elementy zbioru nie mają kolejności, ' \
           'ewentualne rozwiązanie to zamienienie zbioru na listę lub można usunąć wskazany element np. 1' \
           f'\ntX = {x} \ntY = {y}' \
           f'\nUsunięte wtedy go zamieniono na listę: {new_list}'


def zad7(x, y):  # 7. Przekopiuj wszystkie elementy zbioru X do zbioru Y.
    new_set = x.union(y)
    return f'Zad7: {new_set}'  # Jak użyć metody copy w zbiorach


def zad8(x, y):  # 8. Wypisz na ekran część wspólną zbiorów X oraz Y.
    return f'zad8: {x.intersection(y)}'


print(f'X: {X}  a:{a}')
print(f'Y: {Y}  b:{b}')

print('')
print(zad1(X))  # zadnie 1
print(zad2(X, Y))  # zadnie 2
print(zad3(X, Y))  # zadnie 3 i 4
print(zad5(X, Y))
print(zad6(X, Y))
print(zad7(X, Y))
print(zad8(X, Y))
