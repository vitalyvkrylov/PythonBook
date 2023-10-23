from graphics import *

win = GraphWin("Окно с фигурами", 500, 500)
while True:
    click = win.getMouse()
    x = click.getX()
    y = click.getY()
    shape = input("круг или квадрат?? ").lower().strip()
    if shape == "круг":
        radius = input("Радиус: ")
        circle = Circle(Point(x, y), int(radius))
        circle.draw(win)
    elif shape == "квадрат":
        side = input("длина стороны: ")
        square = Rectangle(Point(x, y), Point(x + int(side), y + int(side)))
        square.draw(win)