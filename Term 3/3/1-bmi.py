import tkinter as tk


root = tk.Tk()


L1= tk.Label(root, text='Weight')
L1.grid(row=0, column=0)

E1= tk.Entry(root,)
E1.grid(row=0, column=1)

L2= tk.Label(root, text='Hight')
L2.grid(row=1, column=0)

E2= tk.Entry(root)
E2.grid(row=1, column=1)

frame = tk.Frame(root)
frame.grid(row=2, column=0, columnspan=2)

B1= tk.Button(frame, text='cancle')
B1.grid(row=2 , column=1)

B2= tk.Button(frame, text='BMI')
B2.grid(row=0 , column=1)

root.mainloop()