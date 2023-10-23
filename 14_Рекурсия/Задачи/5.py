def power(n, tmp, x):
    if tmp <= n:
        if tmp == n:
            return x
        else:
            return power(n, tmp * 2, x + 1)
    else:
        return -1
print(power(int(input('Введите число: ')), 2, 1))