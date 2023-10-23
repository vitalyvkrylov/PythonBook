def word(string):
    for index, c in enumerate(string):
        if string[:index+1].count(c) > 1:
            return c
print(word("программирование на Питон"))
