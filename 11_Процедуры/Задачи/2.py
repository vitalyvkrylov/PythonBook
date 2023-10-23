n = 32
i = k = 0
def f1():
    global n
    global i
    i = pow(n, 2)
    print(i)
f1()
def f2():
    if i > 20:
       k = i / 2
    print(k)
f2()