def procedure(arr1):
  arr1[-1:] = arr2
  if len(arr1) >= 10:
    arr1.reverse()
arr1 = [34, 20, 35, 30, 36, 50]
arr2 = [40, 37, 50, 38, 60]
procedure(arr1)
print(arr1)
