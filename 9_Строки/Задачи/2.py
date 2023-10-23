import itertools
def duplicates(string):
    return ''.join(i for i, _ in itertools.groupby(string))
string = "Программное обеспечение"
print(duplicates(string))
