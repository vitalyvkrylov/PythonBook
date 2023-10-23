measurement = input('Введите номер единицы измерения длины: ')

match measurement:
    case '1':
        print(13 * 0.001)
    case '2':
        print(13 * 0.01)
    case '3':
        print(13 * 0.1)
    case '4':
        print(13 * 1000)
    case _:
        print('Ошибка')