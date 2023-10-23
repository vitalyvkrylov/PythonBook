num_even = -1
number = -1
while number != 0:
    number = int(input('Введите число: '))
    if number % 2 == 0:
        num_even += 1
print(num_even)