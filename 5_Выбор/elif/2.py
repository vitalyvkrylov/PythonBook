import math

x = float(input('Делимое: '))
y = float(input('Делитель: '))
if x % y == 0:
    print(math.sqrt(x / y))
else:
    print(x % y)
