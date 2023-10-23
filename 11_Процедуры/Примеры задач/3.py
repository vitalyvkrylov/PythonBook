n = 5
def f():
    global n
    n = pow(n, 2)
    print(n)
f()