from tkinter import *

root=Tk()

def myClick():
    hello = 'Hello' + e.get()
    myLabel = Label(root, text = hello)
    myLabel.pack()


e = Entry(root,width=50)
e.pack()
e.insert(0,'Enter your name:')

myButton = Button(root,text='Enter Your Stock Quote', command=myClick)
myButton.pack()


root.mainloop()