category = input('Тип транспорта: ')

match category:
    case 'Легковой автомобиль':
        print('B')
    case 'Грузовик':
        print('C')
    case 'Автобус':
        print('D')
    case 'Трамвай':
        print('Tm')
    case _:
        print('Ошибка')