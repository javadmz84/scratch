import tkinter as tk


root = tk.Tk()

conf= {
    'width':5,
    'height':5,
}

label1 = tk.Label(root, text='1', font=('times', 20), cnf=conf)
label1.grid(row=0, column=0)

label2 = tk.Label(root, text='2', font=('times',20), cnf=conf)
label2.grid(row=0, column=1)

label3 = tk.Label(root, text='3', font=('times',20), cnf=conf)
label3.grid(row=1, column=1)

root.mainloop()