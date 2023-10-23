cost = float(input('Введите сумму покупки -> '))
if cost > 1000:
    print('Вам предоставляется скидка 15%!')
    cost = (cost - (cost / 100 * 15))
print('Итог:', cost, ' руб.')