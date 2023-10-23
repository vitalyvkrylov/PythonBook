lst1 = [1, 4, 1, 6]
lst2 = [1, 4, 6]
lst3 = [1, 4, 6, 5, 8, 9]
res1 = list(set(lst1) & set(lst2) & set(lst3))
res2 = [ele + ele for ele in res1]
print(str(res2))

