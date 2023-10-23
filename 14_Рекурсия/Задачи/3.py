def s(lst):
    all = 0
    for n in lst:
        if (type(n) == type([])):
            all = all + s(n)
        else:
            all = all + n
    return all
print(s([[293, 19], [184, 843]]))