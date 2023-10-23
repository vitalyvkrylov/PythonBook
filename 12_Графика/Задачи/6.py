import matplotlib.pyplot as plt

x = [1, 10, 20, 30, 40]
y1 = [2, 6, 5, 7, 15]
y2 = [i*1.2 + 1 for i in y1]
y3 = [i*1.2 + 1 for i in y2]
y4 = [i*1.2 + 1 for i in y3]
plt.figure(figsize=(12, 7))
plt.subplot(221)
plt.plot(x, y1)
plt.subplot(222)
plt.plot(x, y2, ':')
plt.subplot(223)
plt.plot(x, y3, '--')
plt.subplot(224)
plt.plot(x, y4, '-.')
plt.show()