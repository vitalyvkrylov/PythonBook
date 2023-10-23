f = open('C:\\Users\\Admin\\Desktop\\python\\13_Файлы\\1.txt')
s = f.readline()
def two(string):
    return string[:2] if len(string) > 2 else string
print(two(s))