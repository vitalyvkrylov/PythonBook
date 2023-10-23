num = [int(input("Enter a number:"))]
total = 0
for i in num:
    if i == 0:
        break

    total = total + i
    x = int(input("Enter a number(0 to quit):"))
    if x != 0:
        num.append(x)

avg = total / len(num)

print("Counter: ", len(num))
print("The total is: ", total)
print("The average is: ", avg)