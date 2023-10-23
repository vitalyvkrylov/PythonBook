def ln(lst):
    if not lst:
        return 0
    return 1 + ln(lst[1:])
a = [65, 42, 567, 246, 1]
print(ln(a))