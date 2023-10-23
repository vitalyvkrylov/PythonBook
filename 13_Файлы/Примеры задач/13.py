f = open('C:\\Users\\Admin\\Desktop\\python\\13_Файлы\\Примеры задач\\13.txt')
s = f.readline()
def changer(str1):
    return str1[-1:] + str1[1:-1] + str1[:1]
print(changer(s))