import matplotlib.pyplot as plt

x = [1, 10, 20, 30, 40]
y1 = [1, 7, 3, 5, 11]
y2 = [i*1.2 + 1 for i in y1]
y3 = [i*1.2 + 1 for i in y2]
y4 = [i*1.2 + 1 for i in y3]
plt.plot(x, y1, '-.', x, y2, ':', x, y3, '--')
plt.show()