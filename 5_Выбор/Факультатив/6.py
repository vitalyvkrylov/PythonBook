a1 = int(input('Введите координату: '))
a2 = int(input('Введите координату: '))
b1 = int(input('Введите координату: '))
b2 = int(input('Введите координату: '))

print('Да' if (abs(a1 - b1) == abs(a2 - b2)) else 'Нет')