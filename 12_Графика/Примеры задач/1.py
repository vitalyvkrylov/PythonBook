from tkinter import *
root = Tk()
mx = 1000
my = 800
n = Canvas(root, width=mx, height=my)
n.pack()
n.create_oval(0, 10, 100, 100)
root.mainloop()