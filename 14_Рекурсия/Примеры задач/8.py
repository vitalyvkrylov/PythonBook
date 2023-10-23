def com(i, j):
    if (i < j):
        return com(j, i)
    elif (j != 0):
        return (i + com(i, j - 1))
    else:
        return 0
i = 54
j = 4
print(com(i, j))