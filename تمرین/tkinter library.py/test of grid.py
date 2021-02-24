import tkinter as tk

root = tk.Tk()

myLabel1 = tk.Label(root, text='hello world')
myLabel2 = tk.Label(root, text='my name is javad')

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

root.mainloop()
