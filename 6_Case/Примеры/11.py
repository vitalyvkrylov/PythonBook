number = input('Введите цифру: ')

match number:
    case '1':
        print('Один')
    case '2':
        print('Два')
    case '3':
        print('Три')
    case '4':
        print('Четыре')
    case '5':
        print('Пять')
    case '6':
        print('Шесть')
    case '7':
        print('Семь')
    case '8':
        print('Восемь')
    case '9':
        print('Девять')
    case '10':
        print('Десять')
    case _:
        print('Ошибка')
