import matplotlib.pyplot as plt

x = [2, 7, 12, 18, 25]
y = [3, 5, 6, 8, 15]
plt.plot(x, y, label='price of phones')
plt.legend()
plt.grid(True)
plt.show()