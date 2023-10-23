cost = float(input('Введите сумму покупки -> '))
if cost > 1000:
    print('Вам предоставляется скидка 30%!')
    cost = (cost - (cost / 100 * 30))
print('Итог:', cost, ' руб.')


