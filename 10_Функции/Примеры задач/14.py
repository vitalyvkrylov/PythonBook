def summa(lst):
    s = 1
    for x in lst:
        s *= x
    return s
print(summa([64, 2, 91, 7]))