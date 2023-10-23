russian = int(input('Введите балл: '))
math = int(input('Введите балл: '))
physics = int(input('Введите балл: '))
sum = russian + math + physics
if sum >= 240:
    print('Сможет')
else:
    print('Не сможет')