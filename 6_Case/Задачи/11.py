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
    case '6':
        print('Июня')
    case '7':
        print('Июля')
    case '8':
        print('Август')
    case '9':
        print('Сентябрь')
    case '10':
        print('Октябрь')
    case '11':
        print('Ноябрь')
    case _:
        print('Ошибка')
