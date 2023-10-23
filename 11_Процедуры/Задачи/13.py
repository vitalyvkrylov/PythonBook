def procedure(arr):
  if len(arr) % 2 == 1:
    arr.sort(key=lambda x: abs(x), reverse=False)
  else:
    arr.sort(key=lambda x: abs(x), reverse=True)
arr = [19487, 184, 481, 838, 14, 81, 2918]
procedure(arr)
print(arr)