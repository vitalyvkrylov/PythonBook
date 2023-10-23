from graphics import *
win = GraphWin("Треугольник", 200, 200)
triangle = Polygon(Point(50, 150), Point(100, 50), Point(150, 150))
triangle.draw(win)
win.getMouse()
win.close()