x = float(input('Кол-во тетрадок: '))
y = float(input('Кол-во линеек: '))
z = float(input('Кол-во ластиков: '))
if x * 10 + y * 5 + z * 2 <= 50:
    print('Хватит')
else:
    print('Не хватит')