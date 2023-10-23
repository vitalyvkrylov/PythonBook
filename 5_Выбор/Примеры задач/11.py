import math

a = float(input('Коэффицент a -> '))
b = float(input('Коэффицент b -> '))
c = float(input('Коэффицент c -> '))
d = b ** 2 - 4 * a * c
if d >= 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(x1, x2)
else:
    print('Отрицательный дискриминант!')