month = input('Введите месяц: ')

match month:
    case '1':
        print('31 день')
    case '2':
        print('29 дней')
    case '3':
        print('31 день')
    case '4':
        print('30 дней')
    case '5':
        print('31 день')
    case '6':
        print('30 дней')
    case '7':
        print('31 день')
    case '8':
        print('31 день')
    case '9':
        print('30 дней')
    case '10':
        print('31 день')
    case '11':
        print('30 дней')
    case '12':
        print('31 день')
    case _:
        print('Ошибка')