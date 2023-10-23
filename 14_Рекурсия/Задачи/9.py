def connect(n):
    if n == []:
        return n
    if isinstance(n[0], list):
        return(connect(n[0]) + connect(n[1:]))
    return(n[:1] + connect(n[1:]))
n = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(connect(n))