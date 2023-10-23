def lst(l):
    x = []
    for n in l:
        if n not in x:
            x.append(n)
    return x
print(lst([12, 44, 90, 44, 243, 12, 899, 44]))
