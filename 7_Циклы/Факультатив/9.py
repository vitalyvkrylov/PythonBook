import math

for n in range(0, 50):
    for x in range(1, 100000):
        if math.sqrt(x) < n:
            print(x)