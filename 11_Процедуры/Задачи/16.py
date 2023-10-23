def positive():
  print("Неверное число")
n = float(input('Введите положительное число: '))
if n < 0 or n == 0:
  positive()
else:
    print(pow(n, 2))