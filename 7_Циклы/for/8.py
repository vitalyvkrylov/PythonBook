count_zero = 0
for number in range(int(input('Введите количество: '))):
    if int(input('Введите число: ')) == 0:
        count_zero += 1
print(count_zero)