def procedure(arr1):
  if len(arr1) <= 7:
    if len(arr2) % 2 == 1:
      arr1[-1:] = arr2
      arr1.sort(key=lambda x: abs(x), reverse=True)
arr1 = [124, 67, 391]
arr2 = [917, 847, 10]
procedure(arr1)
print(arr1)
