def string(str1):
    return ''.join(reversed(str1))
text = input('Введите строку: ')
count = [i for i in range(len(text))]
print(''.join(text[i].upper() if (i % 2 != 0) else text[i] for i in count))