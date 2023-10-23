count = 0
f = open('C:\\Users\\Admin\\Desktop\\python\\13_Файлы\\12.txt')
s = f.readline()
def changer(str1):
    return str1[-1:] + str1[1:-1] + str1[:1] and ''.join(reversed(str1))
print(changer(s))