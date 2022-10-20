from random import randint
n = int(input())
def f(n):
    a = []
    for i in range(n):
        a +=[randint(1,100)]
    print(a)
    Delta = int(input())
    global k
    k = 0
    for i in range(n):
        if a[i] - min(a) == Delta:
            k+=1
f(n)
print(k)