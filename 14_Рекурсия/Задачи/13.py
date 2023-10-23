def simplicity(n, div = None):
    if div is None:
        div = n - 1
    while div >= 2:
        if n % div == 0:
            print("Число не простое")
            return 0
        else:
            return simplicity(n, div - 1)
    else:
        print("Число простое")
        return 1
n = int(input("Введите число: "))
simplicity(n)