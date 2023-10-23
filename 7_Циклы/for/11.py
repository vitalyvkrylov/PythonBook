number1 = int(input('Введите число: '))
number2 = int(input('Введите число: '))
if number1 < number2:
    for numbers in range(number1, number2 + 1):
        print(numbers)
else:
    for numbers in range(number1, number2 - 1, -1):
        print(numbers)