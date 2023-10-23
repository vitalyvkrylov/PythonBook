def composition(a, b):
    if a == b:
        return "Диапазон введен неверно."
    if a > b:
        a, b = b, a
    res = 1
    for i in range(a, b + 1):
        res *= i
    return res
print(composition(int(input("Введите a: ")), int(input("Введите b: "))))