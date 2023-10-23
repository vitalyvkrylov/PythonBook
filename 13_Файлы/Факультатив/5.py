with open('5.txt') as f:
	text = f.read()
	print(sum(map(str.isalpha, text)), 'Букв')
	print(len(text.split()), 'Слов')
	print(text.count('\n') + 1, 'Строк')