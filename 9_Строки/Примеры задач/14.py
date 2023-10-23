def changer(string):
    if len(string) % 7 == 0:
        return ''.join(reversed(string))
        return string
print(changer('экзамен'))