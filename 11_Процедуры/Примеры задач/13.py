n = 21
def f():
    global n
    if n > 19:
        n = pow(n, 3)
        print(n)
f()