def m2(i, j):
    if i > j:
        return i
    return j
def m3(i, j, p):
    return m2(i, m2(j, p))
print(m3(492, 1030, 504))
