def sum_sequence(seq):
    if len(seq) == 1:
        return seq[0]
    else:
        return seq[0] + sum_sequence(seq[1:])
print(sum_sequence([3, 6, 9, 12, 15, 18, 21]))