import math

ring_radius = int(input('Радиус кольца (см) -> '))
hole_radius = int(input('Радиус отверстия (см) -> '))

if hole_radius < ring_radius:
    print('%.2f' % (math.pi * (ring_radius ** 2 - hole_radius ** 2)))
else:
    print('Ошибка! Радиус отверстия должен быть меньше радиуса кольца.')