http_code = input('Введите код http: ')

match http_code:
    case '200':
        print('OK')
    case '404':
        print('Не найдено')
    case '418':
        print('Я чайник')
    case _:
        print('Код не найден')