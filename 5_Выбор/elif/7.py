bread = int(input('Введите цену: '))
ice_cream = int(input('Введите цену: '))
soda = int(input('Введите цену: '))
cheese = int(input('Введите цену: '))
sum = bread + ice_cream + soda + cheese
if sum > 440:
    print('Не хватит')
else:
    print('Хватит')