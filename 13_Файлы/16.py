f = open('C:\\Users\\Admin\\Desktop\\python\\13_Файлы\\16.txt')
s = f.readline()
def change(str1):
  symbol = str1[0]
  str1 = str1.replace(symbol, '*')
  str1 = symbol + str1[1:]
  if len(s) % 2 != 0:
    return ''.join(reversed(str1))
print(change(s))