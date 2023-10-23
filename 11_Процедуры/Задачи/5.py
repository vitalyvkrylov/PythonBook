def procedure(arr1):
    if len(arr1) < 10:
        arr2.append(79)
    arr1.sort(key=lambda x: abs(x), reverse=False)
arr1 = [48, 57, 12, 44, 98, 342]
arr2 = arr1
procedure(arr1)
print(arr2)