quantity_number = int(input('Введите количество: '))
sum = 0
for number in range(1, quantity_number + 1):
    sum += number ** 3
print(sum)