import math

x = float(input('Введите число: '))
y = (math.sqrt(math.e**(2.2*x)) - abs(math.sin((math.pi*x)/(x + 2/3)))) + 1.7
print('%.3f' % y)