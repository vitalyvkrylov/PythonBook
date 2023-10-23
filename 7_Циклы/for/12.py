number1 = int(input('Введите число: '))
number2 = int(input('Введите число: '))
for numbers in range(number1 - (number1 + 1) % 2, number2 - number2 % 2, -2):
    print(numbers, end=' ')