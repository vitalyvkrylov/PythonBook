def string(text):
	for line in text.split('\n'):
	    return(' '.join(line.split()[::-1]))
print(string("Привет, Питон!"))