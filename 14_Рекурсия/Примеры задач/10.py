def entry(str1, n):
    if not str1:
        return 0
    elif str1[0] == n:
        return 1 + entry(str1[1:], n)
    else:
        return entry(str1[1:], n)
str1 = input("Введите строку: ") #видеокарта - устройство в составе компьютера, которое выводит картинку на экран, буква
n = input("Введите букву: ") #о
print(entry(str1, n))