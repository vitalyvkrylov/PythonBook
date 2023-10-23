def procedure(arr):
    arr.sort(key=lambda x: abs(x), reverse=False)
arr = [54, 87, 520, 92, 1]
procedure(arr)
print(arr)