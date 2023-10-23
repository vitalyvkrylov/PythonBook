import itertools
def procedure(arr1):
    index = arr1.index(93)
    arr1[index] = 1
    arr1.sort(key=lambda x: abs(x), reverse=True)
arr1 = [532, 1810, 39181, 93, 51, 9840]
arr2 = [13, 4]
procedure(arr1)
print(list(itertools.permutations(arr2)), arr1)