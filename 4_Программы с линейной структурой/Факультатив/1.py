U = int(input('Напряжение: '))
R = int(input('Сопротивление: '))
t = 5
I = U / R
A = U * I * t
print('Сила тока: ', I)
print('Работа тока: ', A)