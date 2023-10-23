fin = {}
f = open('6.txt', 'r')
for strings in f:
    key, val = len(strings), strings
    fin[key] = fin.get(key, [])+[val]
for n, i in sorted(fin.items()):
    print('{} ({}): {}'.format(n, len(i), ' '.join(sorted(i))))
