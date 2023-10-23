def change(arr):
    first_symbol = arr.pop()
    end_symbol = arr.pop(0)
    arr.append(end_symbol)
    arr.insert(0, first_symbol)
    return arr
print(change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
