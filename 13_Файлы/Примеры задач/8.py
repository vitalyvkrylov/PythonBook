count = 0
f = open('C:\\Users\\Admin\\Desktop\\python\\13_Файлы\\Примеры задач\\8.txt')
count = f.read().count('e')
if count:
    print(count)
else:
        print('Такого элемента нету')