fruits = ['Яблоки', 'Груши', 'Апельсины', 'Мандарины', 'Бананы']
fruits.sort()
citrus = input('Сколько цитрусовых продуктов? ')
len_word = input('Какова длина самого длинного слова? ')
if citrus == '2' and len_word == '9':
        print('Ответ правильный')
        print(len(max(fruits, key=len)))
        print(fruits)
else:
    print('Ответ неправильный')

