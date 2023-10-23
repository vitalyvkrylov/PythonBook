'''for A in range(100, 0, -1):
    k = 0
    for x in range(1, 1000):
        F = (((90 % A) == 0) and ((not(x % A) == 0) <= (((x % 15) == 0) <= ((not(x % 20) == 0)))))
        if F == 1:
            k = k + 1
    if k == 999:
        print(' A -> ', A)
        break'''
'''for A in range(100, 0, -1):
    k = 0
    for x in range(1, 1000):
        F = (((120 % A) == 0) and (((x % 36) == 0) <= ((not(x % A) == 0 <= (not(x % 45) == 0)))
        if F == 1:
            k = k + 1
    if k == 999:
        print(' A -> ', A)
        break

'''
'''for A in range(100, 0, -1):
    k = 0
    for x in range(1, 1000):
        F = ((120 % A) == 0) and (((x % 36) == 0) <= ((not(x % A) == 0) <= (not(x % 45) == 0)))
        if F == 1:
            k = k + 1
    if k == 999:
        print(' A -> ', A)
        break'''
for A in range(1000, 0, -1):
    k = 0
    for x in range(1, 1000):
        F = (A % 40 == 0) and ((780 % x == 0) <= ((not(A % x) == 0) <= (not(180 % x) == 0)))
        if F == 1:
            k = k + 1
    if k == 999:
        print(' A -> ', A)
        #break
