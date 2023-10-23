import math

x = float(input('Введите число: '))
y = abs(math.sin(x) * math.tan(x)) * 1 / math.sqrt(2)
print('%.2f' % y)