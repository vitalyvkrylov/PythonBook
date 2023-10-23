def count_paths(i, j):
    if i == 1 or j == 1:
        return 1
    else:
        return count_paths(i - 1, j) + count_paths(i, j - 1)
print(count_paths(4, 4))