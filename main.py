text = 'Pierwsze zdanie. Drugie zdanie, z przecinkiem. ' \
       'Trzecie zdanie z wykrzyknikiem! ' \
       'Czwarte zdanie to pytanie? ' \
       'I ostatnie piąte zdanie.'  # W tekście mamy: 5 zdań, 15 słów i 107 liter


def remove_punctuation(txt):  # funkcja usuwająca interpunkcje z podanego tekstu
    from string import punctuation
    remove_punctuation_from_txt = txt
    for p in punctuation:  # punctuation z modułu string zawiera wszystkie znaki interpunkcyjne
        remove_punctuation_from_txt = remove_punctuation_from_txt.replace(p, '')
    return remove_punctuation_from_txt


def letters(txt):  # funkcja zliczająca litery
    text_check = remove_punctuation(txt)
    text_check = text_check.replace(' ', '')
    return len(text_check)


def words(txt):  # funkcja zliczająca słowa
    text_check = remove_punctuation(txt)
    words_count = 0
    for word in text_check.split(' '):
        if len(word) >= 2:  # Ignoruje słowa krótsze niż dwa znaki
            words_count += 1
    return words_count


def sentences():
    pass  # TODO: Napisać funkcje zliczającą zdania
    # UWAGA! Zdanie może kończyć się kropką, znakiem zapytania lub wykrzyknikiem


print(text)  # tekst oryginalny
print(words(text))  # test zliczania słów
print(letters(text))  # test zliczania liter
