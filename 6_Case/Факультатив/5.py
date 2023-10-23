year = int(input('Введите две последних цифры года: '))
day = int(input('Введите день: '))
month = int(input('Введите месяц: '))

visokos = 0
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    visokos = 1
else:
    visokos = 0
if day > 31 or day <= 0:
    print('День некорректный')
if month > 12 or month <= 0:
    print('Месяц некорректный')

match year:
    case '1':
        if month > 12 or month <= 0:
            print('Месяц некорректный')
        else:
            match month:
                case '1':
                    if day != 31:
                        print('День некорректный')
                    else:
                        print('Дата корретная')
                case '2':
                    if day != 29:
                        print('День некорректный')
                    else:
                        print('Дата корретная')
                case '3':
                    if day != 31:
                        print('День некорректный')
                    else:
                        print('Дата корретная')
                case '4':
                    if day != 30:
                        print('День некорректный')
                    else:
                        print('Дата корретная')
                case '5':
                    if day != 31:
                        print('День некорректный')
                    else:
                        print('Дата корретная')
                case '6':
                    if day != 30:
                        print('День некорректный')
                    else:
                        print('Дата корретная')
                case '7':
                    if day != 31:
                        print('День некорректный')
                    else:
                        print('Дата корретная')
                case '8':
                    if day != 30:
                        print('День некорректный')
                    else:
                        print('Дата корретная')
                case '9':
                    if day != 31:
                        print('День некорректный')
                    else:
                        print('Дата корретная')
                case '10':
                    if day != 30:
                        print('День некорректный')
                    else:
                        print('Дата корретная')
                case '11':
                    if day != 31:
                        print('День некорректный')
                    else:
                        print('Дата корретная')
                case '12':
                    if day != 30:
                        print('День некорректный')
                    else:
                        print('Дата корретная')
    case '0':
        if month > 12 or month <= 0:
            print('Месяц некорректный')
        else:
            match month:
                case '1':
                    if day != 31:
                        print('День некорректный')
                    else:
                        print('Дата корретная')
                case '2':
                    if day != 28:
                        print('День некорректный')
                    else:
                        print('Дата корретная')
                case '3':
                    if day != 31:
                        print('День некорректный')
                    else:
                        print('Дата корретная')
                case '4':
                    if day != 30:
                        print('День некорректный')
                    else:
                        print('Дата корретная')
                case '5':
                    if day != 31:
                        print('День некорректный')
                    else:
                        print('Дата корретная')
                case '6':
                    if day != 30:
                        print('День некорректный')
                    else:
                        print('Дата корретная')
                case '7':
                    if day != 31:
                        print('День некорректный')
                    else:
                        print('Дата корретная')
                case '8':
                    if day != 30:
                        print('День некорректный')
                    else:
                        print('Дата корретная')
                case '9':
                    if day != 31:
                        print('День некорректный')
                    else:
                        print('Дата корретная')
                case '10':
                    if day != 30:
                        print('День некорректный')
                    else:
                        print('Дата корретная')
                case '11':
                    if day != 31:
                        print('День некорректный')
                    else:
                        print('Дата корретная')
                case '12':
                    if day != 30:
                        print('День некорректный')
                    else:
                        print('Дата корретная')





