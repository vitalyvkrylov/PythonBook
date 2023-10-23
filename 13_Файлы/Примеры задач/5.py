import os

f = open('C:\\Users\\Admin\\Desktop\\python\\13_Файлы\\Примеры задач\\5.txt', 'r')
print(f.name)
f.close()
os.rename(f.name,'C:\\Users\\Admin\\Desktop\\python\\13_Файлы\\Примеры задач\\5_1.txt')
f = open('C:\\Users\\Admin\\Desktop\\python\\13_Файлы\\Примеры задач\\5_1.txt', 'r')
print(f.name)
f.close()