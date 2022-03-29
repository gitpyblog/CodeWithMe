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


def logowanie(password):
    test = password
    while test != 'qwerty':
        test = input('podaj hasło: ')
    else:
        print('zalogowano')


logowanie(input('podaj hasło: '))
