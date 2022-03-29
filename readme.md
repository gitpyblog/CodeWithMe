### Podstawowe struktury danych

`None` - wartość nieokreślona

`str` - ciąg znaków

`int` - liczba całkowita

`float` - liczba zmiennoprzecinkowa

`bool` - wartość logiczna True/False

`list` - lista, sekwencja wartości którą, można rozszerzać

`tuple` - krotka, sekwencje niezmiennych wartości

`set` - zbiór, kolekcje unikatowych wartości, automatycznie usuwa wszystkie powtórzenia

`dict` - słownik, zbiór kluczy z wartościami

### Operatory arytmetyczne

`+` - dodawanie

`-` - odejmowanie

`/` - dzielenie

`//` - dzielenie całkowite, zwraca całości w dzielnej

`%` - dzielenie modulo, zwraca resztę z dzielenia

`*` - mnożenie

`**` - potęgowanie

`-x` - liczba przeciwna

### Operatory logiczne

`==` - równe

`!=` - różne

`=<` - równe lub mniejsze

`=>` - równe lub większe

`< >` - większe, mniejsze

`and` - i

`or` - lub

`is` - jest

`is not` - nie jest

`in` - w

### Pętle

```python
while True:
    number = 1
    if number == 1:
        break
```

```python
for x in range(10):
    print(x)
```

### Przydatne metody i funkcje wbudowane:

`len()` - zliczania długość obiektu

`count()` - zlicza ilość wystąpień danego argumenty w sprawdzanej wartości

`find()` - sprawdza wystąpienie podanej wartość

`capitalizer()` - sprawdza wyraz zaczyna się od dużej litery

`min(), max()` - zwraca najmniejszy/największy element

`sum()` - Zwraca sumę elementów

`startswift = "ARG", endswift = "ARG"` - sprawdza wystąpienie argumentu na początku/końcu

`replace(ARG1, ARG2)` - zamienia jedną wartość na drugą

`split('SEPARATOR')` - krojenie ciągu znaków z wykorzystaniem separatora

`find()` - Szuka podanej wartości

`upper(), lower()` - zmienia litery na wielkie/małe

`reverse()` - odwrócenie

### Przykładowe fragmenty kodu

```python
hello = 'Hello - World'
print(hello[2:])  # wycinamy od drugiego znaku
print(hello[:2])  # wycinamy pierwsze dwa znaki
print(hello[2:4])  # kroimy od drugiego do czwartego znaku
print(hello[-2:])  # ucinamy ostatnie dwa znaki
print(hello[:-1:-3])  # ucinamy od ostatniego do trzeciego znaku od końca

print(hello.lstrip('He'))  # Wycinamy podany ciąg od lewej
print(hello.rstrip('ld'))  # Wycinamy podany ciąg od prawej
print(hello.replace('Hello', 'Hi'))  # Zamieniamy w formatowanym ciągu jedną wartość na drugą

pets = 'pies', 'kot', 'papuga'
for index, animal in enumerate(pets, start=1):
    print(f'{index} - {animal}')

```
