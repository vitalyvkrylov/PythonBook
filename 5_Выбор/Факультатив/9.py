x = int(input('Кооордината x: '))
y = int(input('Координата y: '))
if x >= 0 and y >= 0:
    print('1')
if x <= 0 and y >= 0:
    print('2')
if x <= 0 and y <= 0:
    print('3')
if x >= 0 and y <= 0:
    print('4')