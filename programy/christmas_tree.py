def christmas_tree(level):
    for i in range(level+1):
        star = '* ' * i
        print(star.center(level * 2, ' '))
    print('|||'.center(level * 2, ' '))


christmas_tree(int(input('Podaj ilość poziomów choinki: ')))