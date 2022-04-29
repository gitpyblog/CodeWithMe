import numpy
import pandas as pd

# SERIES
# Obiekt series jest analogią do kolumny excela, mozę posaidać nagłowk, macierz musi być kwadratowa
panda = pd.Series(['ala', 'ola', 'ela'])
# print(panda)


# numpy.array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0, like=None)
'''
dtype - typ danych
        complex -> liczby zespolone
        pozostałe typy: https://numpy.org/doc/stable/user/basics.types.html
ndmin - minimalny wymiar w tablicy
    
'''

wiersz1 = ['imię', 'rasa', 'wiek']
wiersz2 = ['Misiu', 'Brytyjczyk', 7]
test = numpy.array([wiersz1, wiersz2, ['Molek', 'Brytyjczyk', 8]])
# print(test)

# s = pandas.Series(data=numpy.arange(1, 10, 1.5), index=numpy.arange(0, 6), dtype='float')
s = pd.Series(data=numpy.arange(1, 10, 1.5), index=['a', 'b', 'c', 'd', 'e', 'f'], dtype='float')
# print(s)

data = {
    'Name':
        ['Tom', 'Joseph', 'Krish', 'John'],
    'Age':
        [20, 21, 19, 18]
}

df = pd.DataFrame(data)
df.index += 1
# df.index = ['a', 'b', 'c', 'd']
# print(df)

# koty = pandas.read_excel('koty.xlsx')
# print('nasz excel:', koty)


stocks = {'PLW': 387.00, 'CDR': 339.5, 'TEN': 349.5, '11B': 391.0}
quotations = pd.Series(data=stocks)

'''
Cw. 5: Przekształć obiekt quotations do obiektu DataFrame. Ustaw nazwę kolumny na price.
'''
quotations = pd.DataFrame(quotations, columns=['price'])
# print(quotations)
# quotations.columns = ['cena']
# print(quotations)
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
# class pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)


'''
Cw. 6: Dodaj dwa elementy:
    indeks: BBT, wartość: 25.5
    indeks: F51, wartość: 19.2
'''
# https://pandas.pydata.org/docs/reference/api/pandas.concat.html#pandas.concat
# stocks2 = {'PLW': 387.00, 'CDR': 339.5, 'TEN': 349.5, '11B': 391.0}
# quotations2 = pd.Series(data=stocks)

stocks = {'PLW': 387.00, 'CDR': 339.5, 'TEN': 349.5, '11B': 391.0}
quotations2 = pd.Series(data=stocks)

quotations2 = quotations2.append(pd.Series({'BBT': 25.5, 'F51': 19.2}))
# print(quotations2)

# s1 = pd.Series({'BBT': 25.5, 'F51': 19.2})
# quotations2 = quotations2.append(s1)
# print(quotations2)

# zamiana na DataFrame ->
# quotations2 = pd.DataFrame(data=quotations2, columns=['price'])
# print(quotations2)
# quotations2.index = range(1, 7)
# quotations2.index = ['a','x','g',1,2,3]
# print(quotations2.loc[3]) # loc/iloc -> slicing obiektów w pandas
# print(quotations2.max)

# print(quotations2.set_index('price', inplace=True))
# quotations2.sort_values(ascending=True)
# print(quotations2)

'''    
Cw. 7: Obiekt quotations z poprzedniego ćwiczenia przekształć do obiektu typu DataFrame.
'''
# quotations2 = pd.DataFrame(data=quotations2, columns=['price'])

'''
Cw. 8: Zresetuj indeks i nadaj nazwy kolumn 'ticker' oraz 'price'
'''

# quotations = pd.DataFrame(quotations).reset_index()
# quotations.columns = ['ticker', 'price']
# print(quotations)


'''
Cw. 9: Zbuduj poniższy obiekt DataFrame i przypisz do zmiennej companies:
data_dict = {
    'company': ['Amazon', 'Microsoft', 'Facebook'],
    'price': [2375.00, 178.6, 179.2],
    'ticker': ['AMZN.US', 'MSFT.US', 'FB.US']
}
'''

data_dict = {
    'company': ['Amazon', 'Microsoft', 'Facebook'],
    'price': [2375.00, 178.6, 179.2],
    'ticker': ['AMZN.US', 'MSFT.US', 'FB.US']
}

campanies = pd.DataFrame(data_dict)
# print(campanies)


'''
Cw. 10 Przekształć pierwszą kolumnę obiektu companies w indeks.
'''

campanies.set_index('company')
# print(campanies)

'''
Cw. 11 Wytnij wiersz dla spółki Facebook z obiektu companies
'''
print(campanies.iloc[2]) # lub campanies.loc['Facebook']
print(campanies)
companies.loc['Microsoft', 'price']
companies.iloc[1, 0]

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

