month = input('Введите месяц: ')

match month:
    case '12':
        print('Зима')
    case '1':
        print('Зима')
    case '2':
        print('Зима')
    case '6':
        print('Лето')
    case '7':
        print('Лето')
    case '8':
        print('Лето')
    case _:
        print('Ошибка')