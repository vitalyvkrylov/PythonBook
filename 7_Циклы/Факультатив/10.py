for n in range(100000, 333333, 3):
    if n % 8 and n % 10 and n % 7 != 7 and n % 13 != 13:
        print(n)