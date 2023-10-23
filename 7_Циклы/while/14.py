number = -11
while number < 0:
    number += 1
    if number == -5:
        print('Цифра -5 не входит в цикл.')
        continue
    print(number)
