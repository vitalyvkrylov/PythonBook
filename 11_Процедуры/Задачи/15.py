def num(i):
    for n in range(5):
        print(i)
symbol = float(input('Введите число: '))
if symbol < 10:
    num(symbol)
else:
    print('Ошибка. Введенное число больше 10.')