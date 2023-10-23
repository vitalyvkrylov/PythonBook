def summa(lst):
    s = 1
    for x in lst:
        s *= x
    return s
print(summa([24, 9, 47, 15]))
