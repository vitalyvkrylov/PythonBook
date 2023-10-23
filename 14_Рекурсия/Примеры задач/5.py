def gcd(i, j):
    if (j == 0):
        return i
    else:
        return gcd(j, i % j)
i = int(input("Введите первое число: "))
j = int(input("Введите второе число: "))
divider = gcd(i, j)
print(divider)