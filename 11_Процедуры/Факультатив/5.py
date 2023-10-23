def divider(n):
    min_divider = n
    max_divider = 1
    count_div = 0
    for i in range(3, n // 2):
        if (n % i == 0):
            if (min_divider > i):
                min_divider = i
            if (max_divider < i):
                max_divider = i
            if (n % i == 0):
                count_div += 1
    print(count_div)
    print(min_divider)
    print(max_divider)
divider(10234)