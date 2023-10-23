import math

a = float(input('Коэффицент a -> '))
b = float(input('Коэффицент b -> '))
c = float(input('Коэффицент c -> '))
d = b ** 2 - 4 * a * c
if d >= 0:
    print('Решение есть')
else:
    print('Решения нет')