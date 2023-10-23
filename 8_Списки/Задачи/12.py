def list(arr):
    arr.sort(key=lambda x: abs(x), reverse=False)
    return arr
print(list([67, 28, 7, 41, 92, 26, 18, 62, 58]))
