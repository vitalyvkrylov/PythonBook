from graphics import *
import random

win = GraphWin("Угадай число", 300, 200)
message = Text(Point(150, 50), "Угадай число от 1 до 100")
message.draw(win)
number = random.randint(1, 100)
entry = Entry(Point(150, 100), 5)
entry.draw(win)
button = Rectangle(Point(125, 130), Point(175, 170))
button.setFill("light blue")
button.draw(win)
label = Text(Point(150, 150), "Угадать")
label.draw(win)
while True:
    click = win.getMouse()
    if button.getP1().getX() <= click.getX() <= button.getP2().getX() and button.getP1().getY() <= click.getY() <= button.getP2().getY():
        guess = int(entry.getText())
        if guess < number:
            message.setText("Слишком маленькое.")
        elif guess > number:
            message.setText("Слишком большое.")
        else:
            message.setText("Вы угадали!")
            break
win.getMouse()
win.close()