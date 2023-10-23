from tkinter import *
import time
import random
root = Tk()
mx = 1000
my = 800

n = Canvas(root, width=mx, height=my)
n.pack()
ball = n.create_oval(0, 10, 100, 100, fill = '#{:06x}'.format(random.randint(0,256**3)))
while True:
    for x in range((mx - 100) // 10):
        n.move(ball, 10, 0)
        root.update()
        time.sleep(0.0005)

    for x in range((my - 100) // 10):
        n.move(ball, 0, 10)
        root.update()
        time.sleep(0.0005)

    for x in range((mx - 100) // 10):
        n.move(ball, -10, 0)
        root.update()
        time.sleep(0.0005)

    for x in range((my - 100) // 10):
        n.move(ball, 0, -10)
        root.update()
        time.sleep(0.0005)
root.mainloop()