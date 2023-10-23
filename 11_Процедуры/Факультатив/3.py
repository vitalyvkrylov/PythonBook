def procedure(a, b, c, d, e, f, g, h):
    pos_count, neg_count = 0, 0
    for num in a, b, c, d, e, f, g, h:
        if num >= 0:
            pos_count += 1
        else:
            neg_count += 1
    print(pos_count, neg_count)
procedure(0, 5, -2, -1, -1, 3, 5, 8)
