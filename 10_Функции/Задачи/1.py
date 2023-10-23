def string(str2):
    str1 = ''
    a = len(str2)
    while a > 0:
        str1 += str2[a - 1]
        a -= 1
    return str1
print(string('информатика'))
