import tkinter as tk
from tkinter import messagebox

def bmi():

    try:
        w = float(e1.get())
        h = float(e2.get())
        index = w / (h*h)
        messagebox.showinfo('Your BMI', f'{index:.2f}')
    except:
        messagebox.showerror('FAILED!', 'Ooops!')

root = tk.Tk()


l2= tk.Label(root, text='Weight(kg)')
l2.grid(row=0, column=0)

e1= tk.Entry(root,)
e1.grid(row=0, column=1)

L2= tk.Label(root, text='Hight(m)')
L2.grid(row=1, column=0)

e2= tk.Entry(root)
e2.grid(row=1, column=1)

frame = tk.Frame(root)
frame.grid(row=2, column=0, columnspan=2)

B1= tk.Button(frame, text='cancle', command=root.destroy)
B1.grid(row=2 , column=1)

B2= tk.Button(frame, text='BMI', command=bmi)
B2.grid(row=0 , column=1)

root.mainloop()