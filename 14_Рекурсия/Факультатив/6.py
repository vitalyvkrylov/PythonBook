def multiply_list(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] * multiply_list(lst[1:])
print(multiply_list([5, 7, 2]))