result = 0
for s in open('9.txt'):
    result += int(s.strip())
print(result)