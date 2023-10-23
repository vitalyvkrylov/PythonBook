def procedure(string):
    index = string.index(5813)
    string[index] = 818
    string.sort(key=lambda x: abs(x), reverse=False)
string = [819, 125, 39, 1, 5813, 900, 3481, 37, 12, 54]
procedure(string)
print(string)