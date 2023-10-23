n = float(input('Введите число: '))
measurement = input('Введите единицу измерения: ')
con = input('Введите номер единицы измерения длины: ')
'''g --> g = 1
g --> kg = 2
g --> t = 3
kg --> kg = 4
kg --> g = 5
kg --> t = 6

t --> t = 7
t --> g = 8
t --> kg = 9'''
match measurement:
    case 'g':
        match con:
            case '1':
                print(n * 1)
            case '2':
                print(n / 1000)
            case '3':
                print(n / 1000000)
    case 'kg':
        match con:
            case '4':
                print(n * 1)
            case '5':
                print(n * 1000)
            case '6':
                print(n / 1000)
    case 't':
        match con:
            case '7':
                print(n * 1)
            case '8':
                print(n * 1000000)
            case '9':
                print(n * 1000)
    case _:
        print('Ошибка')