D = int(input('Диаметр: '))
corner = int(input('Градусная мера: '))

pi = 3.14
R = D / 2
S = pi * R**2
l = (pi * R)/180 * corner
print('Радиус: ', R)
print('Площадь круга: ', '%.2f' % S)
print('Длина дуги: ', '%.2f' % l)