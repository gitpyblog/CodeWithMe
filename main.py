from Algorithms import *

# Odczyt pliku tekstowego do analizy
with open('dyktando.txt', 'r', encoding='utf-8') as plik:  # W tekście mamy: 5 zdań, 15 słów i 107 liter
    text_sample = plik.read()

# zapis wyników analizy do osobnego pliku
with open('dyktando-wyniki.txt', 'w', encoding='utf-8') as plik_w:  # W tekście mamy: 5 zdań, 15 słów i 107 liter
    wyniki = f'Litery: {letters(text_sample)}, Słowa: {words(text_sample)}, Zdania: {sentences(text_sample)}'
    plik_w.write(wyniki)
