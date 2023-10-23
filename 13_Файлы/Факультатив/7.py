f = open('7.txt', 'r')
f = [line.rstrip() for line in f]
res = []
letters = "aAeEiIoOuU"
for sub in f:
    flag = False
    for e in letters:
        if sub.startswith(e):
            flag = True
            break
    if flag:
        res.append(sub)
res.sort()
print(str(res))