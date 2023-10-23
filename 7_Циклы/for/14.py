print('Введите целое число от 23 до 287: ')
for number in range(23, 287):
    x = int(input())
    number = str(bin(x)[2:])
    if x > 287 or x < 0:
        print('Ошибка')
    else:
        print('Десятичному числу', x, 'соответствует двоичное', number)