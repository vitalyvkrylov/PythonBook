n = int(input('Введите число: '))
c = 0
for i in range(0, 1000):
    if 2 ** i == n:
        c += 1
        print(i)
if c == 0:
    print("НЕТ")