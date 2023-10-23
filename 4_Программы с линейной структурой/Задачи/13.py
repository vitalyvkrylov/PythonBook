time = float(input('Введите число -> '))
hours = time / 60
min = time % 60
print('%.0f' % hours, 'ч.','%.0f' % min, 'мин.')