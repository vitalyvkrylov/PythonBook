def lst(l):
    a = []
    for n in l:
        if n % 2 == 1:
            a.append(n)
    return a
print(lst([54, 29, 40, 2, 7, 328, 72, 11, 9]))