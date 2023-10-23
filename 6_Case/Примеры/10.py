measurement = input('Введите номер единицы измерения массы: ')

match measurement:
    case '1':
        print(13 * 0.000001)
    case '2':
        print(13 * 0.001)
    case '3':
        print(13 * 1000)
    case _:
        print('Ошибка')