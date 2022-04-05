# używając pętli for wypisz wszystkie sześciany liczb od 1 do 10
# numbers = list(range(1, 11))
# for i in numbers:
#     i = i ** 3
#     print(i, end=', ')

# używając pętli while wypisz wszystkie liczby podzielne przez 3, mniejsze od 50
# l = 0
# max = 50
# while l < max:
#     if l % 3 == 0:
#         print(l, end=', ')
#     l += 1

# używając pętli if ... else sprawdz czy wylosowana liczba z przedziału (-100,100) jest dodatnia
# import random

# while True:
#     liczba_los = random.randint(-100, 100)
#     print(liczba_los)
#     if liczba_los > 0:
#         break

# liczba_los = random.randint(-100, 100)
# while liczba_los > 0:
#     print(liczba_los)
#     break


# def logowanie(haslo_user, max_log):
#     proba_log = 1
#     haslo = None
#     while haslo != haslo_user:
#         haslo = input(f'({proba_log} proba logowania) podaj hasło: ')
#         proba_log += 1
#         if proba_log > max_log:
#             print(f'przekroczyłeś ilość dozwolonych prob logowania: ')
#             break
#     else:
#         print('zalogowano')
#         return True
#
#
# logowanie('qwerty', 3)
#
#
# def pass_valid(password, numbers=True, min_length=8):
#     specjalne = ['!', '@']
#     numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     password = min_length
#
#     if len(password) >= 13:
#         print(f'hasło zwiera zbyt dużo znaków, {len(password)}')
#     elif len(password) < 8:
#         print(f'hasło zwiera zbyt mało znaków, {len(password)}')

# pass_valid('abc123ddddddd', numbers=True, min_length=8)  # upper=True, special=True

#
# n = int(input('podaj liczbę: '))
# # 5-9 -> '5-9'
# # 10-15 -> '10-15'
# # 16-20 -> '16-20'
# # 5 6 7 8 9 10 11 12 13 14 15 16 17 19 20
# if n in range(5, 9):
#     print('w zakresie do 5 do 9')
# elif n in range(10, 15):
#     print('w zakresie od 10 do 15')
# elif n in range(16, 20):
#     print('w zakresie od 16 do 20')
#
#
# if n in range(0, 30):
#     print('w zakresie od 0 do 30')
#
#
# if n % 2 == 0:
#     print('parzysta')
# else:
#     print('nieparzysta')

# imię = 'patryk'
# nazwisko = 'kowalski'
# lista = (1, 2, 3, 4, 5)
#
#
# def wyswietl_imie(i, n, x):
#     i = i.title()
#     n = n.upper()
#     if type(x) != list:
#         print(f'to nie jest lista, to jest {type(x)}')
#
#     return (f'Twoje imię to: {i}, Twoje nazwisko to: {n}')
#
#
# print(wyswietl_imie(n=nazwisko, i=imię, x=lista))

n = [2, 3, 4, 5, 6, 7, 8]
new_n = list(map(lambda x: x ** 2, n))

print(n)
print(new_n)

# data = [('Ola', 22), ('Amber', 22), ('Alfred', 23), ('Skye', 4), ('Albert', 12), ('Amber', 22), ('Amber', 22)]
# data = [1, 1, 1, 2, 2, 2, 3, 3, 3]
# print(data)
# for x in data:
#     if data.count(x) > 1:
#         data.remove(x)
# print(data)

