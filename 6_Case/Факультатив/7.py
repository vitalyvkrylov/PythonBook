mark = input('Введите оценку: ')

match mark:
    case 'A':
        print(5)
    case 'B':
        print(4)
    case 'C':
        print(3)
    case 'D':
        print(3)
    case 'F':
        print(2)
    case _:
        print('Ошибка')