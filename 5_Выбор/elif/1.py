height = float(input('Рост: '))
weight = float(input('Вес: '))
optimal_weight = height - 100
difference = abs(weight - optimal_weight)
if weight > optimal_weight:
    print('Вам надо похудеть на', difference, 'кг')
elif weight < optimal_weight:
    print('Вам надо поправиться на', difference, 'кг')
else:
    print('С весом все нормально')

