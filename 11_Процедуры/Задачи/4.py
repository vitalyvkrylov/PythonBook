def procedure(string):
    index = string.index(8)
    string[index] = 54
    string.reverse()
string = [817, 8, 92, 26, 320, 8, 40, 11]
procedure(string)
print(string)
