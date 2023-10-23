divider = int(input('Введите делитель -> '))
divisible = int(input('Введите делимое -> '))
if divisible % divider != 0:
    print(divisible % divider)
else:
    print(divisible - divider)