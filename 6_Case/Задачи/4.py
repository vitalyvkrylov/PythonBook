http_code = input('Введите код http: ')

match http_code:
    case '100 - 199':
        print('Информационный')
    case '200 - 299':
        print('Успешный')
    case '300 - 399':
        print('Перенаправление')
    case '400 - 499':
        print('Клиентские ошибки')
    case '500 - 599':
        print('Серверные ошибки')
    case _:
        print('Код не найден')