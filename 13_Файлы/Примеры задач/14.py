f = open('C:\\Users\\Admin\\Desktop\\python\\13_Файлы\\Примеры задач\\14.txt')
s = f.readline()
def lst(l):
    x = []
    for n in l:
        if n not in x:
            x.append(n)
    return x
print(lst(s))