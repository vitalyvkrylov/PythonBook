def binary_search(arr, start, end, target):
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, start, mid-1, target)
    else:
        return binary_search(arr, mid+1, end, target)

arr = [1, 3, 5, 7, 9, 11, 13]
target = 9
print(binary_search(arr, 0, len(arr)-1, target))