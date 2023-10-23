count = 0
number_quantity = int(input("Введите количество: "))
for _ in range(number_quantity):
    number = int(input("Введите числа: "))
    if number < 0:
        count += 1
print('Количество отрицательных элементов: ', count)