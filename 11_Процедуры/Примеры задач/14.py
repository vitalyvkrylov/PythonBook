def procedure(arr):
    if len(arr) % 2 == 0:
        arr.sort(key=lambda x: abs(x), reverse=True)
arr = [17, 47, 814, 0, 91, 4, 61, 84]
procedure(arr)
print(arr)