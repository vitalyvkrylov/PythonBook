a = []
def bin_sys(n):
    if (n == 0):
        return a
    division = n % 2
    a.append(division)
    bin_sys(n // 2)
str1 = int(input("Введите число: "))
bin_sys(str1)
a.reverse()
for i in a:
    print(i)