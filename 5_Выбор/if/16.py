import math

x = float(input('Введите число -> '))
if x >= 0:
    print('Корень введенного числа', math.sqrt(x))
else:
    print('Ошибка! Извлекать квадратный корень из отрицательного числа нельзя.')

