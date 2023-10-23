print('Введите целое число от 0 до 255: ')
for number in range(0, 255):
    x = int(input())
    number = str(bin(x)[2:])
    if x > 255 or x < 0:
        print('Ошибка')
    else:
        print('Десятичному числу', x, 'соответствует двоичное', number)