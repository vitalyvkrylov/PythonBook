print('Введите целое число от 456 до 1294: ')
for number in range(456, 1295):
    x = int(input())
    number = str(bin(x)[2:])
    if x > 1294 or x < 0:
        print('Ошибка')
    else:
        print('Десятичному числу', x, 'соответствует двоичное', number)