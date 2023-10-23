def nok(a, b):
    i = min(a, b)
    while True:
        if i % a==0 and i % b==0:
            break
        i += 1
    print(i)
nok(30, 45)