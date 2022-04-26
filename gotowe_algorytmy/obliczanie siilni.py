# 5. Write a Python function to calculate the factorial
# of a number (a non-negative integer). The function accepts the number as an argument.
def silnia(n):
    zakres = list(range(1, n+1))
    result = 1
    for i in zakres:
        result *= i
    return result

# silnia obliczona z zastosowaniem rekurencji
def silnia(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return n * silnia(n - 1)

print(silnia(5))