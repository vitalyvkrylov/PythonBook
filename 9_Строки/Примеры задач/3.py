string = "524.173,69"
maketrans = string.maketrans
string = string.translate(maketrans(' .', '. '))
print(string)