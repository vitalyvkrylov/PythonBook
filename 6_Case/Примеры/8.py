month = input('Введите число: ')

match month:
    case '12':
        print('Декабрь')
    case '1':
        print('Январь')
    case '2':
        print('Февраль')
    case '3':
        print('Март')
    case '4':
        print('Апрель')
    case '5':
        print('Май')
    case _:
        print('Ошибка')