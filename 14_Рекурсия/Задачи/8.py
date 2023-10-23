def changer(line):
    if len(line) == 0:
        return line
    else:
        return changer(line[1:]) + line[0]
a = str(input("Введите строку: "))
print(changer(a))