f = open('C:\\Users\\Admin\\Desktop\\python\\13_Файлы\\Примеры задач\\10.txt')
s = f.readline()
count = 1
maxn = 0
for x in range(len(s) - 1):
    if s[x] == s[x + 1]:
        count += 1
        maxn = max(maxn, count)
    else:
        count = 1
print(maxn)