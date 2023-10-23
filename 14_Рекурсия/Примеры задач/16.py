def summ(a1, len1):
    if len1 == 0:
        return 0
    else:
        return a1[len1 - 1] + summ(a1, len1 - 1)
n = int(input("Введите длину списка: "))
a2 = []
for i in range(0, n):
    el = int(input("Введите элемент списка: "))
    a2.append(el)
b = summ(a2, n)
print(b)