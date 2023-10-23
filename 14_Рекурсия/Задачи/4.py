def step(x, tmp, n, ms):
    if tmp <= x:
        ms += n**2
        return step(x, tmp + 1, n, ms)
    else:
        return ms / 1000
x = 5
n = 40
print(step(x, 2, n, n))