def positive():
  print("Неверное число")
n = int(input('Введите положительное число: '))
if n < 0:
  positive()