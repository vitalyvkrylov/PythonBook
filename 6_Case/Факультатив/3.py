year = int(input('Введите две последних цифры года: '))
day = int(input('Введите день: '))
month = input('Введите код месяца: ')
year_code = (6 + year + year / 4) % 7

match month:
    case '1':
        print((day + 1 + year_code) % 7)
    case '2':
        print((day + 2 + year_code) % 7)
    case '3':
        print((day + 3 + year_code) % 7)
    case '4':
        print((day + 4 + year_code) % 7)
    case '5':
        print((day + 5 + year_code) % 7)
    case '6':
        print((day + 6 + year_code) % 7)
    case '0':
        print((day + 7 + year_code) % 7)
    case _:
        print('Ошибка')