import matplotlib.pyplot as plt

x = [1, 10, 20, 30, 40]
y1 = [2, 6, 5, 7, 15]
y2 = [i*1.2 + 1 for i in y1]
y3 = [i*1.2 + 1 for i in y2]
y4 = [i*1.2 + 1 for i in y3]
plt.plot(x, y1, '-', label='line 1')
plt.plot(x, y2, '--', label='line 1')
plt.legend(bbox_to_anchor=(1, 0.3))
plt.show()