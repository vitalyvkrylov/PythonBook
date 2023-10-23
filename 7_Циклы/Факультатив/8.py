sum_even = 0
sum_odd = 0
for n in range(9, 1, -3):
    if n % 2 == 0:
        sum_even += n
    else:
        sum_odd += n
print(sum_even, sum_odd)
