n = 4
i = k = 0
def f1():
    global n
    global i
    i = pow(n, 2)
    print(i)
f1()
def f2():
    if i < 121:
       k = i**3 - 100
    print(k)
f2()