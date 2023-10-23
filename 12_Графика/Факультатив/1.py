from graphics import *
win = GraphWin('Произвольная фигура', 400, 400)
obj = Polygon(Point(20, 20), Point(400, 70), Point(100, 350), Point(200, 200), Point(90, 90))
obj.setOutline("darkred")
obj.setWidth(10)
obj.setFill("red")
obj.draw(win)
win.getMouse()
win.close()