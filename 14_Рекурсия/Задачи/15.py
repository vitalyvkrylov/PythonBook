def con(n, level):
    if (level == 1):
        return (n)
    if (level != 1):
        return (n * con(n, level - 1))
n = 65
level = 3
print(con(n, level))