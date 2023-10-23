def lst(l):
    x = []
    for n in l:
        if n not in x:
            x.append(n)
    return x
print(lst([88, 73, 73, 29, 88, 56, 39]))