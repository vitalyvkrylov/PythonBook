from graphics import *
import math

win = GraphWin("Окно со спиралью", 200, 200)
a = 3.0
b = 0.2
for t in range(0, 1000):
    x = (a + b * t) * math.cos(t)
    y = (a + b * t) * math.sin(t)
    Point(x + 100, y + 100).draw(win)
win.getMouse()
win.close()