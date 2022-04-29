import pandas

stocks = {'PLW': 387.00, 'CDR': 339.5, 'TEN': 349.5, '11B': 391.0}
quotations = pandas.Series(data=stocks)

'''
Przekształcenie obiektu quotations do obiektu DataFrame. 
Wyświetlanie dwóch różnych nazw dla tej samej kolumny. 
'''
quotations = pandas.DataFrame(quotations, columns=['price'])
print(quotations)

quotations.columns = ['cena']
print(quotations)

# analogicznie działa metoda z .index
