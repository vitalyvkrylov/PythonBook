import math

equation = input('Введите вид уравнения: ')

match equation:
    case 'линейное':
        a = float(input('Коэффициент a -> '))
        b = float(input('Коэффициент b -> '))
        if (a == 0 and b == 0):
            print("Бесконечное количество решений.")
        if (a == 0 and b != 0):
            print("Решений нет.")
        if (a != 0):
            print('%.2f' % (b / a))

match equation:
    case 'квадратное':
        a = float(input('Коэффициент a -> '))
        b = float(input('Коэффициент b -> '))
        c = float(input('Коэффициент c -> '))
        d = b ** 2 - 4 * a * c
        if d >= 0:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            print('%.2f' % x1, '%.2f' % x2)
        else:
            print('Отрицательный дискриминант!')


