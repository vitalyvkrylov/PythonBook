import math

x = float(input('Введите число: '))
y = 1/math.sqrt(x) + math.log(abs(0.2 + math.sin(x)))**2 * pow(x**2, 1.0/3.0)
print('%.4f' % y)