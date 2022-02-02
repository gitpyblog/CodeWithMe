from Algorithms import *

# Pierwsze zdanie. Drugie zdanie, z przecinkiem. Trzecie zdanie z wykrzyknikiem! Czwarte zdanie to pytanie? I ostatnie piąte zdanie.
# W tekście mamy: 5 zdań, 15 słów i 107 liter

# Odczyt pliku tekstowego do analizy
with open('dyktando.txt', 'r', encoding='utf-8') as plik:
    text_sample = plik.read()

# Zapis wyników analizy do nowego pliku
with open('dyktando-wyniki.txt', 'w', encoding='utf-8') as plik_w:  # W tekście mamy: 5 zdań, 15 słów i 107 liter
    wyniki = f'Litery: {letters(text_sample)}, Słowa: {words(text_sample)}, Zdania: {sentences(text_sample)}'
    plik_w.write(wyniki)

# Wydruk wyników analizy
print(f'\n{Mark.REVERSED}Analizuje plik: {Mark.BOLD}{plik_w.name}{Mark.RESET}')
for index, sentence in enumerate(sentences(text_sample)):
    print(f'🟡({index + 1}) {sentence}')

print(f'\n{Mark.BOLD}{Mark.LIGHTYELLOW}Podsumowanie:{Mark.RESET}')
print(f'Znaków: {Mark.BOLD}{characters(text_sample)}{Mark.RESET}')
print(f'Liter: {Mark.BOLD}{letters(text_sample)}{Mark.RESET}')
print(f'Słów: {Mark.BOLD}{words(text_sample)}{Mark.RESET}')
print(f'Zdań: {Mark.BOLD}{len(sentences(text_sample))}{Mark.RESET}\n')
