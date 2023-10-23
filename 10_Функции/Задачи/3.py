def power(nubmer, degree):
    res = 1
    for n in range(abs(degree)):
        res *= nubmer
    if degree >= 0:
        return res
    else:
        return 1 / res
print(power(float(input('Введите число: ')), int(input('Введите степень: '))))