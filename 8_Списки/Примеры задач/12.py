import itertools
arr = [[98, 4, 28, 13], [80, 7], [52, 67, 14], [98, 4, 28, 13], [60, 4, 23]]
arr.sort()
new_arr = list(arr for arr,_ in itertools.groupby(arr))
print(new_arr)