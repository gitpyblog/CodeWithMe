[TOC]


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

```python
x % 2 == 0  # Zwraca 0 dla liczb parzystych
x % 1 == 1 # Zwraca 1 dla liczb nieparzystych
```


### Operatory arytmetyczne
`+` - dodawanie
`-` -   odejmowanie
`/` - dzielenie
`//` -  dzielenie całkowite
`%` -  dzielenie modulo, zwraca całości w dzielnej
`*` - mnożenie
`**` -  potęgowanie
`-x` -  liczba przeciwna


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
