s = 20
h = int(input('Введите высоту трапеции: '))
a = int(input('Введите меньшую сторону основания: '))
b = int(input('Введите большую сторону основания: '))

match s:
    case 20:
        print((a + b)/2 * h)
