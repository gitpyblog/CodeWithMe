data = ([('Ola', 22), ('Amber', 22), ('Alfred', 23), ('Skye', 4), ('Albert', 12), ('Amber', 22), ('Amber', 22)])

for x in data:
    p = data.count(x)
    if p > 1:
        data.remove(x)

