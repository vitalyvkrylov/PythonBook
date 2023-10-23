color = input('Введите цвет: ')

match color:
    case 'Красный':
        print('Стойте')
    case 'Желтый':
        print('Ждите')
    case 'Зеленый':
        print('Едьте')
    case 'Мигающий желтный':
        print('Будьте предельно внимательны')
    case _:
        print('Ошибка')