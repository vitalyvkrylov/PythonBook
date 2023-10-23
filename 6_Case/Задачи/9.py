number = input('Введите число: ')

match number:
    case '15':
        print(103 - 15)
    case '34':
        print(76 + 34)
    case '29':
        print(80 - 29 * 2)
    case _:
        print('Ошибка')
