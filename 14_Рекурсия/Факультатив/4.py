def combinations(i, j):
    if j in [0, i]:
        return 1
    else:
        return combinations(i - 1, j - 1) + combinations(i - 1, j)
print(combinations(8, 6))