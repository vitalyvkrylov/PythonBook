number = int(input('Введите число: '))
degree = int(input('Введите степень: '))
i = 1
result = 1
while i <= degree:
    result *= number
    i += 1
print(result) 