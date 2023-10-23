import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

x = [1, 10, 20, 30, 40]
y1 = [2, 6, 5, 7, 15]
y2 = [3, 8, 5, 4, 7]
fg = plt.figure(figsize=(7, 3), constrained_layout=True)
gs = gridspec.GridSpec(ncols=2, nrows=1, figure=fg)
fig_ax_1 = fg.add_subplot(gs[0, 0])
plt.plot(x, y1)
fig_ax_2 = fg.add_subplot(gs[0, 1])
plt.plot(x, y2)
plt.show()