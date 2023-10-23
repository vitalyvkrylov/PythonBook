abc1 = (input('Введите первый модуль: '))
abc2 = (input('Введите второй модуль: '))
abc3 = (input('Введите третий модуль: '))
n = int(input('Введите целое число x: '))

match abc1:
    case 'x**3 - 2':
        if n**3 - 2 > 0:
            print('x**3 - 2')
        else:
            print('-x**3 + 2')
match abc2:
    case 'x - 1':
        if n - 1 > 0:
            print('x - 1')
        else:
            print('-x + 1')
match abc3:
    case 'x':
        if n > 0:
            print('x')
        else:
            print('-x')