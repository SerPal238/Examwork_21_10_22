from random import randint
n = int(input("Размерность массива А = "))
m = int(input("Размерность массива В = "))
def f(n,m):
    a = [] 
    b = []  
    for i in range(n):
        a += [randint(1,100)]
    for i in range(m):
        b += [randint(1,100)]
    print(a,b)
    c = []
    if n < m:
        for i in range(n):
            if a[i] in b:
                c+=[a[i]]
    else:
        for i in range(m):
            if b[i] in a:
                c+=[b[i]]
    return (set(c))
print(f(n,m))