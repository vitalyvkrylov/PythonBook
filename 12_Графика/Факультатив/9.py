from graphics import *

win = GraphWin("Окно для текста", 500, 500)
text = input("Введите текст: ")
pos_x = int(input("Введите координату x: "))
pos_y = int(input("Введите координату y: "))
label = Text(Point(pos_x, pos_y), text)
label.setSize(20)
label.setStyle("bold")
label.draw(win)
win.getMouse()
win.close()