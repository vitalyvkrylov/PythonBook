import math

def square(x):
    return math.sqrt(x)
i = square(9)
if i // 2 != 0:
    print(-1)
else:
    print(i)