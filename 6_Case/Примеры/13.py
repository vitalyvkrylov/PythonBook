symbol = input('Введите арифметический знак: ')

match symbol:
    case '-':
        print(10 - 5)
    case '+':
        print(10 + 5)
    case '/':
        print(10 / 5)
    case '*':
        print(10 * 5)
    case _:
        print('Ошибка')