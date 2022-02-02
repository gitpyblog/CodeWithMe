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

for index, sentence in enumerate(sentences(text_sample)):
    print(f'{index + 1} 🟡 {sentence}')

print(f'\nLiter: {letters(text_sample)}')
print(f'Słów: {words(text_sample)}')
print(f'Zdań: {len(sentences(text_sample))}')
