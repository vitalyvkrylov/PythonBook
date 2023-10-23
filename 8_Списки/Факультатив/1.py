count5 = count7 = 0
for n in range(100):
    if n % 5 == 0:
        count5 += 1
    if n % 7 == 0:
        count7 += 1
print(count5, count7)