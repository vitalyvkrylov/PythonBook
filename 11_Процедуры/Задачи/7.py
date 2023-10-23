import itertools
def procedure(arr1):
    arr1.sort(key=lambda x: abs(x), reverse=True)
arr1 = [71, 90, 43, 12, 882, 9361, 500, 4]
arr2 = [18, 90]
procedure(arr1)
print(list(itertools.permutations(arr2)), arr1)

