def funk(nazwisko, **kwargs):
    print("Nazwisko:", nazwisko)
    for key, item in kwargs.items():
        print("Imię:", key, "Wiek:", item)


funk("Kowalscy", Ewa=33, Michał=44)
