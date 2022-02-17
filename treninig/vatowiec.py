# napisz funkcję która, będzie obliczała podaną przez User stawkę vat.

class Mark:
    """ Klasa kolorująca tekst """
    VAT = '\033[92m'
    RESET = '\033[0m'  # RESET COLOR


kwota = float(input('podaj kwotę: '))
vat = int(input('podaj stawkę vat: '))


def vatowiec(k, v):
    result = float(k + (k * (v / 100)))
    return result


print(f'''
    wybrana kwota: {Mark.VAT}{kwota}{Mark.RESET},
    wybrana stawka vat: {Mark.VAT}0,{vat}{Mark.RESET},
    brutto: {Mark.VAT}{vatowiec(kwota, vat)}{Mark.RESET} zł''')