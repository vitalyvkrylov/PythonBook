def catalan(n):
    if n == 0:
        return 1
    else:
        return sum([catalan(i) * (n - i - 1) for i in range(n)])
print(catalan(6))