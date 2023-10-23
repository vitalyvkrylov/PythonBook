with open('2.1.txt', 'r') as f1:
  data1 = f1.read().split('\n')
with open('2.2.txt', 'r') as f1:
  data2 = f1.read().split('\n')
data3 = [line for line in data2 if line not in data1]
print(data3)