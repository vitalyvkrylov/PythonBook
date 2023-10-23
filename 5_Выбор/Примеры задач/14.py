toaster = float(input('Цена тостера: '))
teapot = float(input('Цена чайника: '))
pan = float(input('Цена сковородки: '))
knife = float(input('Цена набора ножей: '))
if toaster + teapot + pan + knife <= 9500:
    print('Хватит')
else:
    print('Не хватит')