max = 0
number = -1
while number != 0:
    number = int(input('Введите число: '))
    if number > max:
        max = number
print(max)