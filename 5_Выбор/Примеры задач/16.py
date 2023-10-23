russian = int(input('Введите балл: '))
math = int(input('Введите балл: '))
physics = int(input('Введите балл: '))
sum = russian + math + physics
if sum >= 250:
    print('Сможет')
else:
    print('Не сможет')