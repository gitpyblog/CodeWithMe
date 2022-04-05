def logowanie(haslo_user, max_log):
    proba_log = 1
    haslo = None
    while haslo != haslo_user:
        haslo = input(f'({proba_log} proba logowania) podaj hasło: ')
        proba_log += 1
        if proba_log > max_log:
            print(f'przekroczyłeś ilość dozwolonych prob logowania: ')
            break
    else:
        print('zalogowano')
        return True
