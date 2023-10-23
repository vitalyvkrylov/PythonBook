import math

x = float(input('Введите число -> '))
y = math.sqrt((pow(x, 4/5)) + pow(x, (4 - x)/5)) + math.log(abs(x - 20.5))
print('%.2f' % y)