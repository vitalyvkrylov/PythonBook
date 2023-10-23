from tkinter import *
import random
root = Tk()
mx = 1000
my = 800
n = Canvas(root, width=mx, height=my)
n.pack()
cube = n.create_rectangle(0, 10, 100, 100, fill = '#{:06x}'.format(random.randint(0,256**3)))
root.mainloop()