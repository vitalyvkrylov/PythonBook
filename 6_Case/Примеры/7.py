number = input('Введите число: ')

match number:
    case '20':
        print(90 - 20)
    case '30':
        print(4 * 30)
    case '15':
        print(100 - 15 * 2)
    case _:
        print('Ошибка')