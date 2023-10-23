import math

x = float(input('Введите число: '))
numerator = math.sqrt(1 / 5 + pow(math.e**x, 1.0/5.0))
denominator = (abs(math.log(x**2) - 1.3))
y = numerator / denominator
print('%.3f' % y)