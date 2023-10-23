f = open('C:\\Users\\Admin\\Desktop\\python\\13_Файлы\\Примеры задач\\12.txt')
s = f.readline()
def string(n):
    return ''.join(reversed(n))
print(string(s))