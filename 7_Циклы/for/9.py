number = int(input('Введите число: '))
for i in range(1, number + 1):
    for j in range(1, i + 1):
        print(j, sep='', end='')
    print()