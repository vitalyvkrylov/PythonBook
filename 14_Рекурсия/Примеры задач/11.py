def connect(n):
    if n == []:
        return n
    if isinstance(n[0], list):
        return(connect(n[0]) + connect(n[1:]))
    return(n[:1] + connect(n[1:]))
n = [[543, 205, 736, 5], [95, 35, 245, 821]]
print(connect(n))