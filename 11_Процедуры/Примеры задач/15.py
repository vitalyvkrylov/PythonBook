def f():
  global i, j
  if i % 2 == 0:
    if j % 3 == 0:
      (i, j) = (j, i)
(i, j) = (6, 27)
f()
print(i, j)