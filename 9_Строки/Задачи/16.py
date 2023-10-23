def delete(str1, n):
    part1 = str1[:n]
    part2 = str1[n + 1:]
    return part1 + part2
print(delete('буфер обмена', 2))
