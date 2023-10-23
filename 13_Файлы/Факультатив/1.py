sp = []
f = open('test1.txt', 'r')
for i in range(1, 51):
    x = int(f.readline())
    sp.append(x)
f.close()
sp.sort()
print(sp)
