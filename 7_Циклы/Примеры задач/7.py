count = 0
number = int(input("number: "))
for _ in range(number):
    n = int(input("Введите n: "))
    if n == 0:
        count += 1
print('Количество элементов равных 0: ', count)