russian = int(input('Введите балл: '))
math = int(input('Введите балл: '))
english = int(input('Введите балл: '))
sum = russian + math + english
if sum >= 190:
    print('Сможет')
else:
    print('Не сможет')