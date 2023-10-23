number = float(input('Введите число -> '))
rub = number / 10
cop = number % 10
print('%.0f' % rub, 'руб.', '%.0f' % cop, 'коп.')