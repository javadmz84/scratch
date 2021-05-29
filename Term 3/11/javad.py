from tkinter import *

def j(g):
    if g>0:
        l1['bg']= 'green'
    else:
        l1['bg']= 'red'


def up(v, b):
    v+=1
    b.set(v)
    j(v)



def down(v, b):
    v-=1
    b.set(v)
    j(v)
    


root =Tk()
b1 = Button(root, text='UP', command = lambda: up(int(var1.get()), var1))
b1.grid(row=0, column=0)
var1 = StringVar()
var1.set('0')
l1 = Label(root, textvariable = var1)
l1.grid(row=1, column=0)
b2 = Button(root, text='DOWN', command=lambda: down(int(var1.get()), var1))
b2.grid(row=2, column=0)

root.mainloop()
