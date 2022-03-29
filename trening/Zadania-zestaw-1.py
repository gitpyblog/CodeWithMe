# Utwórz listę zawierającą 10 losowych liczb z zakresu od -100 do 100
from random import sample, randint

lista = list(sample(range(-100, 100), 10))
print(lista)
# lista.sort()
# print(lista)
# W utworzonym liście znajdź największą i najmniejszą liczbę
print('Min: ', min(lista))
print('Max: ', max(lista))

# W utworzonej liście znajdź największą wartość korzystając z pętli for
maximum = lista[0]
for i in lista:
    if maximum < i:
        maximum = i
print(maximum)

minimum = lista[0]
for i in lista:
    if minimum > i:
        minimum = i
print(minimum)

# Podziel listę na dwie równe listy (a i b) zawierające po 5 elementów
a = lista[0:5]
b = lista[5:11]
print('lista a: ', a)
print('lista b: ', b)
# Zsumuj wszystkie elementy w liście a oraz b następnie sprawdź, która jest większa
if sum(a) > sum(b):
    print('suma a jest większa: ', sum(a), sum(b))
else:
    print('suma b jest większa: ', sum(a), sum(b))
# Utwórz słownik, gdzie kluczami będzie lista a, wartościami lista b
set1 = {"a": b}
set2 = {"b": a}
print(set1)
print(set2)
# Połącz ponownie liste a oraz b w jedna liste i posortuj ją w kolejności od min do max
lista3 = a + b
lista3.sort()
print(lista3)

# Usuń wszystkie powtórzenia z utworzonej listy
#
# lista_bez_powtorzen = set(list)
# lista4 = list(sample(range(-100, 100), 10)) * 2
# print(lista4)
# lista4 = set(lista4)

# print('powtórzenia skasowane: ', list(lista4))

# Uzupełnij listę do 10 elementów z zakresu -100 do 100, jeśli w wyniku usunięcia powtórzeń ilość elementów zmniejszyła się
print('przed', lista)
while len(lista) < 10:
    lista.append(randint(-100, 100))

print('po', lista)

# for i len(lista4):
#     if len(lista4) < 10:
#         lista4.append(sample(range(-100, 100))

# Pomnóż pierwszy element z listy z ostatnim elementem lista
print(lista[0] * lista[-1])

# Dodaj piąty element listy do trzeciego element od końca listy
print(lista[4]+lista[-3])


