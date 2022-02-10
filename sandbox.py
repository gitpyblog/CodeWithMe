hello = 'Hello - World'
print(hello[2:])  # wycinamy od drugiego znaku
print(hello[:2])  # wycinamy pierwsze dwa znaki
print(hello[2:4])  # kroimy od drugiego do czwartego znaku
print(hello[-2:])  # ucinamy ostatnie dwa znaki
print(hello[:-1:-3])  # ucinamy od ostatniego do trzeciego znaku od końca

print(hello.lstrip('He'))  # Wycinamy podany ciąg od lewej
print(hello.rstrip('ld'))  # Wycinamy podany ciąg od prawej
print(hello.replace('Hello', 'Hi'))  # Zamieniamy w formatowanym ciągu jedną wartość na drugą

pets = 'pies', 'kot', 'papuga'
for index, animal in enumerate(pets, start=1):
    print(f'{index} - {animal}')
