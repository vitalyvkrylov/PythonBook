import re

str1 = 'Ах,, Варя,, грех у ???ме..ня на уме!! Сколько я, бедн..ая, плакал..а, чего уж я над со...бой не делала!?...'
opt = re.sub(r'[^\w\s]', '', str1)
''.join(sorted(opt))
words = opt.split()
words.sort()
print(words)
