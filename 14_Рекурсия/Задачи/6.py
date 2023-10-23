def dividers(n, tmp, count):
    if tmp > 0:
        if n % tmp == 0:
            count += 1
        return dividers(n, tmp - 1, count)
    else:
        return count
n = 14
print(dividers(n, n, 0))