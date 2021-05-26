from tkinter import *
from time import sleep

def start(v , d):
    global tick
    tick=True
    v = int(v)
    while v:
        if not tick:
            return
        sleep(1)
        v -= 1
        d.set(v)
        root.update()


def stop():
    global tick
    tick=False
    var1.set(var2.get())

root =Tk()
l1 = Label(root, text='Input Time')
l1.place(x=10, y=10)


var1 = StringVar()
e1 = Entry(root, textvariable=var1, width=5)
e1.place(x=90, y=10)

var2 = StringVar()
var2.set('go')
l2 = Label(root, textvariable=var2, width=10, bg='light green')
l2.place(x=70, y=40)

b1 = Button(root, text='Strat', command=lambda:start(var1.get(), var2))
b1.place(x=70, y=60)

b2 = Button(root, text='Stop', command=stop)
b2.place(x=71, y=90)
root.mainloop()