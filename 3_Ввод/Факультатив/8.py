import math

x = float(input('Введите число -> '))
y = math.sqrt(math.e**(2*x) * math.sqrt(x) - (x - 1/3)/x) * abs(math.cos(2.5 * x))
print('%.2f' % y)