def list(arr):
    arr.sort(key=lambda x: abs(x), reverse=True)
    return arr
print(list([3, 78, 34, 15, 20, 12, 8, 24, 2]))

