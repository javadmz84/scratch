from tkinter import *
from time import sleep
root =Tk()

n_1 = StringVar()
n_1.set('input time')
Label (textvariable=n_1).grid(row=0, column=0, padx=10, pady=10)

e1 = Entry(root)
e1.grid(row=0, column=1)



b1 = Button(root, text='start')
b1.grid(row=3, column=0)

b2 = Button(root, text='cancle', command=root.destroy)
b2.grid(row=3, column=1)

root.mainloop()