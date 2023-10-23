def permutations(seq):
    if len(seq) <= 1:
        return [seq]
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i + 1:]
            for permutation in permutations(rest):
                res.append([seq[i]] + permutation)
    return res
print(permutations([1, 2, 3]))