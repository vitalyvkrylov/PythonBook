max = 0
number_max = 0
number = -1
while number != 0:
    number = int(input('Введите число: '))
    if number > max:
        max, number_maximal = number, 1
    elif number == max:
        number_maximal += 1
print(number_maximal)