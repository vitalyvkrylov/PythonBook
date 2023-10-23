month = input('Введите число: ')

match month:
    case '6':
        print('Июня')
    case '7':
        print('Июля')
    case '8':
        print('Август')
    case '9':
        print('Сентярбь')
    case '10':
        print('Октябрь')
    case '11':
        print('Ноябрь')
    case _:
        print('Ошибка')