code1 ='print(54 + 49)'
code2 = """
def summa(i, j):
    return i + j
a = summa(1, 2)
print(a)
"""
exec(code1)
exec(code2)
