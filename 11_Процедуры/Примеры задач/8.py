def procedure(arr):
  arr.sort(key=lambda x: abs(x), reverse=True)
arr = [62, 80, 351, 5, 42, 71]
procedure(arr)
print(arr)

