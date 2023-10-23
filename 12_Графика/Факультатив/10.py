from graphics import *
import time

win = GraphWin("Animation", 200, 200)
circle = Circle(Point(100, 100), 50)
circle.setFill("red")
circle.draw(win)
while True:
    circle.move(5, 0)
    time.sleep(0.1)