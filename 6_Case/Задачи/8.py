a = input('Введите сторону куба: ')

match a:
    case '15':
        print(15**3)
    case '27':
        print(27**3)
    case '43':
        print(43**3)
    case _:
        print('Ошибка')