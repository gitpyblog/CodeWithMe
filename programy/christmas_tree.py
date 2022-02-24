def christmas_tree(level):
    for i in range(1, level):
        star = '* ' * i
        print(star.center(level * 2, ' '))
    print('|||'.center(level * 2, ' '))


christmas_tree(int(input('Podaj ilość poziomów choinki: ')))