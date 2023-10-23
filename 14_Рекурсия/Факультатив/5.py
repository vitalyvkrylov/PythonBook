def generate_subsets(s):
    if not s:
        return [[]]
    else:
        subsets = generate_subsets(s[:-1])
    return subsets + [subset + [s[-1]] for subset in subsets]
print(generate_subsets([1, 2, 3]))