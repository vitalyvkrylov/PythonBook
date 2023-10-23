def getSumOdds(aList):
    total = 0
    for index, element in enumerate(aList):
        if index % 2 == 1:
            total += element
    return total

l = [12, 10, 5, -4, 2, -1, 10, 8, 5]

print(getSumOdds(l))