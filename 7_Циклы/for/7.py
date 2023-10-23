number = int(input('Введите число: '))
partial_factorial = 1
partial_sum = 0
for i in range(1, number + 1):
    partial_factorial *= i
    partial_sum += partial_factorial
print(partial_sum)