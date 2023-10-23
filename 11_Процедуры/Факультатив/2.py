import math

def triangle(a, b, c):
    P = a + b + c
    p = P / 2
    S = math.sqrt(p*(p - a)*(p - b)*(p - c))
    if a + b > c and a + c > b and b + c > a:
        print('Треугольник существует,', 'S = %.2f' % S)
    else:
        print("Треугольник не существует")
triangle(5, 5, 5)