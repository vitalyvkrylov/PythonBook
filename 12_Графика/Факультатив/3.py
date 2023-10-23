from graphics import *

win = GraphWin("Окно с домом", 200, 200)
roof = Polygon(Point(50, 90), Point(100, 50), Point(150, 90))
roof.draw(win)
walls = Rectangle(Point(50, 90), Point(150, 160))
walls.draw(win)
door = Rectangle(Point(80, 130), Point(120, 160))
door.draw(win)
window = Rectangle(Point(60, 100), Point(90, 130))
window.draw(win)
win.getMouse()
win.close()