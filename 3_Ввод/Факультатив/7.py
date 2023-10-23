import math

x = float(input('Введите число -> '))
y = (pow(math.pi**2 - x**2 + 1/math.e, 1.0/3.0)) + (math.tan((x - 1)/x)) + 1/7
print('%.2f' % y)