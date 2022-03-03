a = 7
b = 5 + 20
krotka = (2, 3, 5)
lista = ['ala', 'janek', 'ola']


# funkcja może przyjmować jeden argument ##############################################################################
def funkcja_1(argument):
    print(argument)  # wyświetlamy przekazany argument


funkcja_1(2)  # podstawiamy do argumentu wartość bezpośrednio
funkcja_1(a)  # podstawiamy do argumentu wartości ze zmiennej
funkcja_1(2 + 3 + 5) # możemy też przekazywać jako argument inne obiekty lub dokonywać operacji


# funkcja może przyjmować wiele argumentów ############################################################################
def funkcja_2(argument1, argument2):
    print(argument1 + argument2)  # dodajemy przekazane argumenty


funkcja_2(2, 5)  # podstawiamy do argumentów wartości bezpośrednio
funkcja_2(a, b)  # podstawiamy do argumentów wartości ze zmiennych


# Funkcja może pakować do krotki wiele argumentów tzw. *ARGS ##########################################################
def funkcja_3(*args):
    return args


print(funkcja_3(1, 2, 3))
print(funkcja_3(krotka, 100, 200, 300,
                lista))  # wszytskie podane wartości zostaną spakowane do jednego argumentu (krotki)

for element in funkcja_3(krotka, 100, 200, 300, lista):
    print(element)


# Funkcja może przyjmować jako argument klucz i wartość tzw. **kwargs #################################################
def funkcja_4(**kwargs):
    for key, item in kwargs.items():  # iterując rozbijamy kwarka na klucz(key) i wartość(item)
        print("Imię:", key, "Wiek:", item)


funkcja_4(Ewa=33, Michał=44, Adam=14, Ola=5)
