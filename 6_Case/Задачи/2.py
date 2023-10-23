day = input('Введите номер дня недели: ')

match day:
    case '1':
        print('Рабочий день')
    case '2':
        print('Рабочий день')
    case '3':
        print('Рабочий день')
    case '4':
        print('Рабочий день')
    case '5':
        print('Рабочий день')
    case '6':
        print('\033[31mВыходной')
    case '7':
        print('\033[31mВыходной')
    case _:
        print('Ошибка')