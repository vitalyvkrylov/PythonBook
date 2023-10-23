measurement = input('Введите номер единицы измерения массы: ')

match measurement:
    case '1':
        print(23 * 0.000001)
    case '2':
        print(23 * 0.001)
    case '3':
        print(23 * 1000)
    case _:
        print('Ошибка')