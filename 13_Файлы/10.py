result = 0

with open ('10.txt', 'r') as f:
  str1 = f.read()
str2 = str1.replace('721', '3432')
with open ('10.txt', 'w') as f:
  f.write(str2)

for s in open('10.txt'):
    result += int(s.strip())
print(result)

