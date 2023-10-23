pens = int(input('Введите цену -> '))
notebooks1 = int(input('Введите цену -> '))
notebooks2 = int(input('Введите цену -> '))
count = pens * 15 + notebooks1 * 10 + notebooks2 * 5
discount = count - count * 0.15
print(discount)