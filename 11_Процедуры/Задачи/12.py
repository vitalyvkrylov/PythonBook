def procedure(string):
  index = string.index(485)
  string[index] = 734
  string.sort(key=lambda x: abs(x), reverse=True)
string = [194, 873, 5000, 41, 485, 9284, 195, 4]
procedure(string)
print(string)
