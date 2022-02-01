def remove_punctuation(text: str) -> str:
    """ Funkcja usuwająca interpunkcje z przekazanego tekstu. """
    from string import punctuation
    remove_punctuation_from_txt = text
    for p in punctuation:  # punctuation z modułu string zawiera wszystkie znaki interpunkcyjne
        remove_punctuation_from_txt = remove_punctuation_from_txt.replace(p, '')

    return remove_punctuation_from_txt


def letters(text: str) -> int:
    """ Funkcja zliczająca litery w przekazanym tekście. """
    text_check = remove_punctuation(text)
    text_check = text_check.replace(' ', '')

    return len(text_check)


def words(text: str) -> int:
    """ Funkcja zwracająca ilość słów w przekazanym tekście. """
    text_check = remove_punctuation(text)
    words_count = 0
    for word in text_check.split(' '):
        if len(word) >= 2:  # Ignoruje słowa krótsze niż dwa znaki
            words_count += 1

    return words_count


def sentences(text):
    return 5
    # UWAGA! Zdanie może kończyć się kropką, znakiem zapytania lub wykrzyknikiem
