f = open('C:\\Users\\Admin\\Desktop\\python\\13_Файлы\\2.txt')
s = f.readline()
def changer(str1):
    if len(str1) % 2 != 0:
        return ''.join(reversed(str1))
print(changer(s))
