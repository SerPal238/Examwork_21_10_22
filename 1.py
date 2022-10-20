from random import random
from random import randint
n = int(input("Размерность массива - "))
def f(n):
    a = [0] * n
    for i in range(n):
        a[i] = randint(0,100) + random()
    print(a)
    c = -1
    for i in range(n):
        if a[i] == max(a):
            c = i
        if c != -1 and i > c:
            a[i] = 0
    return a
print(f(n))