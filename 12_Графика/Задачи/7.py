import matplotlib.pyplot as plt

x = [10, 20, 30, 40, 50]
y1 = [2, 10, 4, 6, 15]
y2 = [2, 5, 3, 12, 17]
plt.plot(x, y1, ':b', label='line 1')
plt.plot(x, y2, '--r', label='line 1')
plt.legend()
plt.show()