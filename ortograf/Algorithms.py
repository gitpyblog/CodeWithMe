# koloruje tekst w terminalu
class Mark:
    """ Klasa kolorująca tekst """
    SUCCESS = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    LIGHTYELLOW = '\033[33m'
    DARKGREY = '\033[90m'
    LIGHTGREY = '\033[37m'
    BOLD = '\033[1m'
    UNDERLINED = '\033[4m'
    REVERSED = "\033[7m"
    RESET = '\033[0m'  # RESET COLOR


# Oczyszczanie ze znaków interpunkcyjnych
def remove_punctuation(text: str) -> str:
    """ Funkcja usuwająca interpunkcje z przekazanego tekstu. """
    from string import punctuation
    remove_punctuation_from_txt = text
    for p in punctuation:
        remove_punctuation_from_txt = remove_punctuation_from_txt.replace(p, '')

    return remove_punctuation_from_txt


# Liczy znaki
def characters(text: str) -> int:
    return len(text)


# Liczy litery
def letters(text: str) -> int:
    """ Funkcja zliczająca litery w przekazanym tekście. """
    text_check = remove_punctuation(text)
    text_check = text_check.replace(' ', '')

    return len(text_check)


def test_letters():
    string_test = 'Pierwsze zdanie. Drugie zdanie, z przecinkiem. Trzecie zdanie z wykrzyknikiem! Czwarte zdanie to pytanie? I ostatnie piąte zdanie.'
    result = letters(string_test)
    assert result == 107
    assert type(result) == int


# Liczy słowa
def words(text: str) -> int:
    """ Funkcja zwracająca ilość słów w przekazanym tekście. """
    text_check = remove_punctuation(text)
    words_count = 0
    for word in text_check.split(' '):
        if len(word) >= 2:  # Ignoruje słowa krótsze niż dwa znaki
            words_count += 1

    return words_count


def test_words():
    string_test = 'Pierwsze zdanie. Drugie zdanie, z przecinkiem. Trzecie zdanie z wykrzyknikiem! Czwarte zdanie to pytanie? I ostatnie piąte zdanie.'
    result = words(string_test)
    assert result == 15
    assert type(result) == int


# Liczy zdania
def sentences(text: str) -> list:
    sentence_endings = '.', '!', '?'
    endings_exceptions = {'itd.', 'itp.', 'al.', 'lek.', 'str.', 'ul.', 'np.', 'przyp.', 'ang.', 'art.', 'arch.', 'br.',
                          'bł.', 'cdn.', 'cyt.', 'dent.', 'dep.', 'doc.', 'dyr.', 'etc.', 'fot.', 'gen.', 'hab.',
                          'inst.', 'inż.', 'jw.', 'ks.', 'lek.', 'm.in.', 'r.', }  # TODO: skróty dwukropkowe
    endings_indexes = [-1]
    sentences_list = list()

    def sentence_slicer(endpoint):
        x = text[endings_indexes[endpoint] + 1:endings_indexes[endpoint + 1] + 1].strip()
        return x

    for index, char in enumerate(text):
        if char in sentence_endings and any(x in text[index - 5:index + 1] for x in endings_exceptions) is False:
            endings_indexes.append(index)

    for index, _ in enumerate(endings_indexes):
        if endings_indexes[index] != endings_indexes[-1]:
            sentences_list.append(sentence_slicer(index))

    return sentences_list


def test_sentences():
    string_test = 'Pierwsze zdanie. Drugie zdanie, z przecinkiem. Trzecie zdanie z wykrzyknikiem! Czwarte zdanie to pytanie? I ostatnie piąte zdanie.'
    result = sentences(string_test)
    assert result == ['Pierwsze zdanie.', 'Drugie zdanie, z przecinkiem.', 'Trzecie zdanie z wykrzyknikiem!',
                      'Czwarte zdanie to pytanie?', 'I ostatnie piąte zdanie.']
    assert type(result) == list
