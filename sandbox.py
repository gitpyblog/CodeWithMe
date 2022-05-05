import pandas

'''
Przydatne funkcje:
    🟢 .set_index - ustawienie danej kolumny jako indeksu
    🟢 .reset_index - resetuje indeks do wartości domyślnych
    🟢 .is_unique - sprawdza czy wartości są unikalne
    🟢 .loc (nazwa od locate) - przeszukuje DataFrame po indeksach np koty.loc['Molek']
    🟢 .iloc - bardzo podobna do loc, z tą różnicą, że funkcja iloc korzysta tylko i wyłącznie z wartości
        numerycznych indeksów. Nawet jeżeli indeks wierszy jest ustawiony na region i nawet jeżeli nasze
        kolumny mają nazwy, funkcją iloc przyjmie tylko numery wierszy i kolumn
    🟢 .head() - wyświetli 5 pierwszych rekordów
    🟢 .tail() - wyświetli 5 ostatnich rekordó

'''

koty = pandas.read_csv('koty.csv')

# Funkcje do odczytu danych to: read_csv(), read_excel(), read_json(), read_pickle(), read_sql()
# Do zapisu analogicznie służą: to_csv(), to_excel(), to_json(), to_pickle(), to_sql(), to_html()

# Wyświetlanie pierwszych trzech rekordów za pomocą slicingu
# print(koty[:3])


# Wyświetlanie konkretnych kolumn (w nawiasach kwadratowych podajemy ich nazwy)
# print(koty[['imie', 'wiek']])


# iloc(wiersze,kolumny) wyświetli konkretne wiersze i kolumny
# print(koty.iloc[2:3, 0:2])


# Umożliwia odniesienie się do konkretnych komórek, za pomocą numeru wiersza oraz nazwy kolumny
# print(koty.loc[1:3], ['imie', 'wiek'])


# Za pomocą funkcji copy() wyraźnie poinformujemy Pandas o tym, że jest to kopia, i powinna mieć nowe miejsce w pamięci.
# Możemy skopiować tylko wybrane przez nas kolumny, np. koty[['imie', 'wiek']].copy()
koty_kopia = koty.copy()

# Możemy dokonywać operacji na wybranych kolumnach, np. podzielić wszystkie wartości przez 2
# koty_kopia['wiek'] /= 2


# Tworzenie nowej kolumny i przypisanie jej domyślnej wartości.
koty_kopia['Nowa kolumna'] = 0

# Zmiana nazwy danej kolumny
koty_kopia = koty_kopia.rename(columns={'Nowa kolumna': 'Właściciel'})

# iterrows() zwraca index wiersza oraz zawartość wiersza (iteracja po wierszach)
# Przeglądamy populację kotów, jeżeli wiek kota jest większy niż 10 lat, ustawia informacje Tak w nowej kolumnie Senior.
# for index, row in koty_kopia.iterrows():
#     if row['wiek'] > 10:
#         koty_kopia.loc[index, 'Senior'] = 'Tak'
#     else:
#         koty_kopia.loc[index, 'Senior'] = 'Nie'


# Druga funkcja do iteracji, troszkę mniej popularna, za to szybsza. Nie zwraca ona indexu
# for row in koty_kopia.itertuples():
#     if row.wiek > 10:
#         print(f'{row.imie} jest już seniorem')


# Aby sprawdzić jakie wartości unikalne przyjmuje kolumna, wystarczy użyć funkcji unique():
# print(koty_kopia.imie.unique())


# shape zwraca informacje na temat liczby wierszy i liczby kolumn/
# print(koty_kopia.shape)


# Info() oferuje informacje na temat kolumn w naszym zbiorze
# print(koty_kopia.info())


# describe() wyświetli statystyki kolumn (możemy również wykonać dla konkretnej kolumny)
# print(koty_kopia.describe())

# sprawdzanie ilości duplikatów
# print(koty_kopia.duplicated().sum())

# usuwanie duplikatów
# koty_kopia.drop_duplicates()


# kostium = pandas.read_csv('https://analityk.edu.pl/wp-content/uploads/2020/12/Halloween.csv', header=2)
# kostium.set_index('region', inplace=True)
# print(kostium[(kostium['1'] == 'Rabbit') | (kostium['1'] == 'Dinosaur')])

filmy = pandas.read_csv('oscars.csv')
f = filmy.category
print(f[:30])
