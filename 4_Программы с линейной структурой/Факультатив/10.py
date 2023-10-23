x = float(input('Математика: '))
y = float(input('Русский язык: '))
z = float(input('Иностранный язык: '))
k = float(input('Обществознание: '))
probability1 = x * y * z
probability2 = x * y * k
print('Вероятность поступления на специальности: ', '%.2f' % probability1, '%.2f' % probability2)