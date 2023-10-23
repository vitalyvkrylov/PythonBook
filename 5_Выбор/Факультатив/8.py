n = int(input('Сторона n: '))
m = int(input('Сторона m: '))
k = int(input('Количество убранных плиток: '))
if m * n - k >= 0:
    print('Да')
else:
    print('Нет')