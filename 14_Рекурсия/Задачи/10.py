def ln(lst):
    if not lst:
        return 0
    return 1 + ln(lst[1:])
a = [1, 2, 3, 4, 5]
print(ln(a))