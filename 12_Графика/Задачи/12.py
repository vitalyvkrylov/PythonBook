from tkinter import *
def button_clicked():
    print (u"Кнопка активирована")
root=Tk()
button1 = Button()
button1.pack()
button2 = Button(root, bg="blue", text=u"Нажмите!", command=button_clicked)
button2.pack()
root.mainloop()