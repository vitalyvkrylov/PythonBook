import math
def ctg(x):
    return 1 / math.tan(x)
x = float(input('Введите число -> '))
y = pow(1/3 * math.sin(x)**5 * math.tan(3*x), 1/9) / ctg(math.cos(128*x/93))
print('%.2f' % y)