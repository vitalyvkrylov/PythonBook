count = 0
number = int(input("Введите количество: "))
for _ in range(number):
    n = int(input("Введите числа: "))
    if n > 0:
        count += 1
print('Количество положительных элементов: ', count)