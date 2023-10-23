import itertools
arr = [[19, 32, 4], [94, 1, 16], [52, 84], [19, 32, 4], [52, 84], [22, 802, 4]]
arr.sort()
new_arr = list(arr for arr,_ in itertools.groupby(arr))
print(new_arr)
