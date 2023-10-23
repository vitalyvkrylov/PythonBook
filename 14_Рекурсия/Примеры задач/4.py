def recurs(n):
    if n < 2:
        return n % 2 == 0
    return recurs(n - 2)
n = int(input("Введите число: ")) #14
if recurs(n) == 1:
      print("Число четное")
else:
      print("Число нечетное")