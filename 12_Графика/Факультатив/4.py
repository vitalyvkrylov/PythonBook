from graphics import *
import random

win = GraphWin("Окно с дождем", 200, 200)
num_drops = 20
drops = []
for i in range(num_drops):
    drops.append(Circle(Point(random.uniform(0, 200), random.uniform(-50, 150)), 2))
for drop in drops:
    drop.draw(win)
while True:
    for drop in drops:
        drop.move(0, 5)
        if drop.getCenter().getY() > 200:
            drop.move(-200, -250)
    update(50)
win.close()