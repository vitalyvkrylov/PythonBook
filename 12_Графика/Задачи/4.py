import matplotlib.pyplot as plt

phones = ['iPhone', 'Samsung', 'Honor', 'Xiaomi', 'Nokia']
cost = [80000, 35000, 20000, 15000, 10000]
plt.bar(phones, cost)
plt.title('Phones')
plt.xlabel('Сompany')
plt.ylabel('Cost')
plt.show()