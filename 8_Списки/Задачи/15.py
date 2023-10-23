def change(arr):
    first_symbol = arr.pop()
    end_symbol = arr.pop(0)
    arr.append(end_symbol)
    arr.insert(0, first_symbol)
    return arr
print(change([54, 302, 36, 17, 83, 45, 10]))
