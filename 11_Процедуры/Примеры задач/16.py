def procedure(arr):
    if len(arr) % 2 != 0:
        arr.sort(key=lambda x: abs(x), reverse=False)
arr = [48, 1, 50, 629, 3011, 4, 37]
procedure(arr)
print(arr)