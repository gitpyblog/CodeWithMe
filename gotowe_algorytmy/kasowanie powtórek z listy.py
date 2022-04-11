data = [('Ola', 22), ('Amber', 22), ('Alfred', 23), ('Skye', 4), ('Albert', 12), ('Amber', 22), ('Amber', 22)]
lista = [7, 7, 7, 7, 1, 1, 2, 3, 4, 5, 5]


# za pomocą pętli for

def doubbles(szufladka):
    new_list = []
    for i in szufladka:
        if i not in new_list:
            new_list.append(i)
    return new_list


print(doubbles(data))
print(doubbles(lista))
