def pal(n):
    if len(n) < 1:
        return 1
    else:
        if n[0] == n[-1]:
            return pal(n[1:-1])
        else:
            return 0
a = str(input("Введите текст: "))
if (pal(a) == 1):
    print("Это палиндром")
else:
    print("Это не палиндром")