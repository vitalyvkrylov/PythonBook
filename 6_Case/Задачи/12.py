estimation = input('Введите оценку: ')

match estimation:
    case '5':
        print('Отлично')
    case '4':
        print('Хорошо')
    case '3':
        print('Удовлетворительно')
    case '2':
        print('Неудовлетворительно')
    case '1':
        print('Плохо')
    case _:
        print('Ошибка')