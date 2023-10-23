count = 0
f = open('C:\\Users\\Admin\\Desktop\\python\\13_Файлы\\4.txt')
for group in f:
    if '@' in group:
        count += 1
if count > 1:
    print(count)
else:
    print('Такого элемента нету')