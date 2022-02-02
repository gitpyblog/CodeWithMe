# a = 'eus', 'lua', 'aja'
# b = 'Mateusz'
#
# print(any(x in b for x in a))


def csv_reader():
    for row in open('ortografia.csv', 'r', encoding='utf-8'):
        yield row


while True:
    word = input('Słowo: ')
    for i in csv_reader():
        i = i.replace('\n', '')
        if word == i:
            print(f'Znalezione: {i}')
            break

