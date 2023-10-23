def change(str1):
  symbol = str1[0]
  str1 = str1.replace(symbol, '€')
  str1 = symbol + str1[1:]
  return str1
print(change('enternet'))