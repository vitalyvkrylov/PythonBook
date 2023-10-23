a = input('Введите сторону куба: ')

match a:
    case '12':
        print(12**3)
    case '23':
        print(23**3)
    case '56':
        print(56**3)
    case _:
        print('Ошибка')