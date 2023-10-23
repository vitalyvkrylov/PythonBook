result = 0
for s in open('11.txt'):
    result += int(s.strip())
if result % 2 == 0:
    print(result)
else:
    print(result / 2)