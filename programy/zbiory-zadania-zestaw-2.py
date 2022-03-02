# ZADANIE 2 - NFZ ====================================================================================================
# załóżmy, że pesel ma 4 cyfry


# stwórzmy zbiór NFZ – ludzie, w bazie pacjentów NFZ
NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
# stwórzmy zbiór chorzy_rok – ludzie chorzy w ostatnim roku
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
# stwórzmy zbiór chorzy_miesiac – ludzie chorzy w ostatnim miesiącu
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
# stwórzmy zbiór krzyki – wszystkich ludzi mieszkających na krzykach
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
# stwórzmy zbiór centrum – wszystkich ludzi mieszkających we Wrocławiu
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
# stwórzmy zbiór wszystkich pacjętów - baza główna
zbior_pusty = set()

print(NFZ, '(NFZ oryginalny)', len(NFZ))
print(NFZ.union(centrum), '(NFZ z centrum)', len(NFZ.union(centrum)))
print(NFZ.union(krzyki), '(NFZ z krzykami)', len(NFZ.union(krzyki)))
print(NFZ.union(chorzy_miesiac), '(NFZ chorzy miesiąc)', len(NFZ.union(chorzy_miesiac)))
print(NFZ.union(chorzy_rok), '(NFZ chorzy rok)', len(NFZ.union(chorzy_rok)))

for i in chorzy_rok:
    NFZ.add(i)

for i in chorzy_miesiac:
    NFZ.add(i)

for i in krzyki:
    NFZ.add(i)

for i in centrum:
    NFZ.add(i)

print('PODSUMOWANIE: ', NFZ, len(NFZ))

# podzielmy zbiór na kobiety i mężczyzn wg peseli
