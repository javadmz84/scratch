import tkinter as tk
import tkinter.ttk as ttk


def register():
    pass

root = tk.Tk()

notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0)

frame1 = ttk.Frame(notebook, width=200, height=280)
frame2 = ttk.Frame(notebook, width=200, height=280)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

notebook.add(frame1, text='Register')
notebook.add(frame2, text='Search')

##################################
tk.Label(frame1, text='Full Name:').grid(row=0, column=0)
tk.Label(frame1, text='ID Num:').grid(row=1, column=0)
tk.Label(frame1, text='Phone').grid(row=2, column=0)

fullname = tk.StringVar()
tk.Entry(frame1, textvariable=fullname).grid(row=0, column=1)

idnumber = tk.StringVar()
tk.Entry(frame1, textvariable=idnumber).grid(row=1, column=1)

phone = tk.StringVar()
tk.Entry(frame1, textvariable=idnumber).grid(row=2, column=1)

tk.Button(frame1, text='Register', command=register).grid(row=3, column=0)
tk.Button(frame1, text='Cancle', command=root.destroy).grid(row=4, column=0)

root.mainloop()