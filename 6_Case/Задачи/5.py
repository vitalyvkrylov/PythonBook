symbol = input('Введите арифметический знак: ')

match symbol:
    case '-':
        print(20 - 5)
    case '+':
        print(20 + 5)
    case '/':
        print(20 / 5)
    case '*':
        print(20 * 5)
    case _:
        print('Ошибка')