def f(s):
    if len(s) == 1:
        return s
    return s[0] + '*' + f(s[1:-1])
s = input('Введите строку: ') #Питон
print(f(s))