s = 'Мама Папа - семья'
count = 0
vowels = set("яыиеаоюэуЯЫИЕАОЮЭУ")
for letter in s:
    if letter in vowels:
        count += 1

def sentence(str1):
   str1 = list(str1)
   for n in str1:
       if n in 'яыиеаоюэуЯЫИЕАОЮЭУ':
          str1.remove(n)
   return str(''.join(str1))
print(sentence(s), count)