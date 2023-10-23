def f():
    global i, j
    (i, j) = (j, i)
i, j = 14, 69
f()
print(i, j)