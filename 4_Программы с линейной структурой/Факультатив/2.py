import math

a = int(input('Сторона квадрата: '))
S = a**2
d = math.sqrt(a**2 + a**2)
print('Площадь квадрата: ', S)
print('Диагональ квадрата: ', '%.2f' % d)