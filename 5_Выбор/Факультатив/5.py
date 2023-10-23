a = int(input('Сторона a: '))
b = int(input('Сторона b: '))
c = int(input('Сторона c: '))
if a < b + c and b < a + c and c < a + b:
    print('Да')
else:
    print('Нет')