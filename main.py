import math

x = str(input())
x = x.split(' ')
numbers = [int(i) for i in x]
n = numbers[0]
k = numbers[1]



# if y > x or len(numbers)>2 :
#     print(0)
# elif y == 1 or y == x: print(1)
# else:
#     a = math.factorial(x)
#     b = math.factorial(y)
#     div = a // (b*(x-y))
#     print(div)


def Newton(n, k):
    Wynik = 1
    for i in range(1, k + 1):
        Wynik = Wynik * (n - i + 1) / i
    return int(Wynik)

print(Newton(n, k))
