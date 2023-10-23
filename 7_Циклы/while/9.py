sum = 0
len = 0
number = int(input('Введите число: '))
while number != 0:
    sum += number
    len += 1
    number = int(input('Введите число: '))
print(sum / len)