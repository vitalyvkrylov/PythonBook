corner = input('Введите количество углов: ')

match corner:
    case '3':
        print('Треугольник')
    case '4':
        print('Четырехугольник')
    case '5':
        print('Пятиугольник')
    case '6':
        print('Шестиугольник')
    case '7':
        print('Семиугольник')
    case '1':
        print('Ошибка')
    case '2':
        print('Ошибка')
    case _:
        print('Многоугольник')