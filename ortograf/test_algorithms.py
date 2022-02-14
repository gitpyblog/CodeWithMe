from algorithms import *

# W tekście mamy: 5 zdań, 15 słów i 107 liter 130 znaków
string_test = 'Pierwsze zdanie. Drugie zdanie, z przecinkiem. Trzecie zdanie z wykrzyknikiem! Czwarte zdanie to pytanie? I ostatnie piąte zdanie.'


def test_remove_punctuation():
    from string import punctuation
    before = 'Ala ma kota' + punctuation
    after = 'Ala ma kota'
    result = remove_punctuation(before)
    assert result == after


def test_characters():
    result = characters(string_test)
    assert result == 130
    assert type(result) == int


def test_letters():
    result = letters(string_test)
    assert result == 107
    assert type(result) == int


def test_words():
    result = words(string_test)
    assert result == 15
    assert type(result) == int


def test_sentences():
    result = sentences(string_test)
    assert result == ['Pierwsze zdanie.',
                      'Drugie zdanie, z przecinkiem.',
                      'Trzecie zdanie z wykrzyknikiem!',
                      'Czwarte zdanie to pytanie?',
                      'I ostatnie piąte zdanie.']
    assert type(result) == list
