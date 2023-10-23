import os

f = open('C:\\Users\\Admin\\Desktop\\python\\13_Файлы\\8.txt', 'r')
print(f.name)
os.rename(f.name,'C:\\Users\\Admin\\Desktop\\python\\13_Файлы\\тестовое задание.txt')
f = open('C:\\Users\\Admin\\Desktop\\python\\13_Файлы\\тестовое задание.txt', 'r')
print(f.name)
f.close()