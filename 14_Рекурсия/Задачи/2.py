def noc(a, b):
    noc.mult= noc.mult + b
    if ((noc.mult % a == 0) and (noc.mult % b == 0)):
        return noc.mult
    else:
        noc(a, b)
    return noc.mult
noc.mult = 0
a = 520
b = 14
if (a > b):
    noc1 = noc(b, a)
else:
    noc1 = noc(a, b)
print(noc1)