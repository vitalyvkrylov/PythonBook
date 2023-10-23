count = 0
f = open('C:\\Users\\Admin\\Desktop\\python\\13_Файлы\\Примеры задач\\9.txt')
for group in f:
    if 'y' in group:
        count += 1
if count > 1:
    print(count)
else:
    print('Такого элемента нету')