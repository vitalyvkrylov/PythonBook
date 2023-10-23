def procedure(arr):
  if len(arr) % 2 == 0:
    arr.sort(key=lambda x: abs(x), reverse=True)
arr = [847, 929, 152, 904, 271, 69, 2, 1500, 27]
procedure(arr)
print(arr)