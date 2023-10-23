R = int(input('Радиус: '))
h = int(input('Высота: '))
m = int(input('Масса: '))
pi = 3.14
V = pi * R * h
p = m / V
print('Объем: ', V)
print('Плотность: ', '%.2f' % p)