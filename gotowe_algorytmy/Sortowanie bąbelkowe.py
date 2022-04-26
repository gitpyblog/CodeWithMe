# 1. Napisz funkcję Pythona, aby znaleźć maksymalną liczbę trzech liczb

def maksik(licz1, licz2, licz3):
    if licz1 > licz2 and licz1 > licz3:
        return licz1
    elif licz2 > licz3 and licz2 > licz1:
        return licz2
    else:
        return licz3

    # return max(licz1, licz2, licz3)

    # liczby = licz1, licz2, licz3
    # result = sorted(liczby)
    # return result[-1]


# print(maksik(244, -5454, 45))


# Algorytm sortowania bąbelkowego:
def bubblesort(elements):
    # Looping from size of array from last index[-1] to index [0]
    for n in range(len(elements) - 1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i + 1]:
                # swapping data if the element is less than next element in the array
                elements[i], elements[i + 1] = elements[i + 1], elements[i]

