import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 10)
y = x
plt.title('Линейная зависимость y = x')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.plot(x, y, 'r--')
plt.show()