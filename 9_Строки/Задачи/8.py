import collections
string = 'антивирус'
letter = collections.defaultdict(int)
for l in string:
    letter[l] += 1
for l in sorted(letter, key=letter.get, reverse=True):
    if letter[l] > 1:
        print('%s %d' % (l, letter[l]))