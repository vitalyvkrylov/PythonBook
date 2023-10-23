n = int(input('Число: '))
max_number = int(input('Число: '))
for i in range(n - 1):
    number = int(input('Число: '))
    if number > max_number:
        max_number = number
print(max_number)