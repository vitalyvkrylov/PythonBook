type = input('Введите тип изделия: ')
bk1 = int(input('Введите цену первого изделия: '))
bk2 = int(input('Введите цену второго изделия: '))
bk3 = int(input('Введите цену третьего изделия: '))
bk4 = int(input('Введите цену четвертого изделия: '))
if bk1 <= 20000:
    revenue1 = bk1 * 0.05
if bk2 > 20000:
    revenue2 = bk2 * 0.03
revenue3 = bk3 * 0.06
revenue4 = bk4 * 0.04

match type:
    case '1':
        print(revenue1)
    case '2':
        print(revenue2)
    case '3':
        print(revenue3)
    case '4':
        print(revenue4)
print(max(revenue1, revenue2, revenue3, revenue4))