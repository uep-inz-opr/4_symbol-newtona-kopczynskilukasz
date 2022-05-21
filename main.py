import math

x = str(input())
x = x.split(' ')
numbers = [int(i) for i in x]
n = numbers[0]
k = numbers[1]

def Newton(n, k):
    Wynik = 1
    for i in range(1, k + 1):
        Wynik = Wynik * (n - i + 1) / i
    return int(Wynik)

print(Newton(n, k))
