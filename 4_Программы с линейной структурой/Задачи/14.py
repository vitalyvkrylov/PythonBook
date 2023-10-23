amount_ontribution = float(input('Введите число -> '))
deposit_term = float(input('Введите число -> '))
interest_rate = float(input('Введите число -> '))
income = (amount_ontribution * interest_rate)/(100 * 365) * deposit_term
sum = amount_ontribution + income
print('%.2f' % income, '%.2f' % sum)