def lst(l):
    a = []
    for n in l:
        if n % 2 == 0:
            a.append(n)
    return a
print(lst([24, 65, 8, 10, 41, 73]))
