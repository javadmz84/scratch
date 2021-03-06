import tkinter as tk
import reg
import tkinter.ttk as ttk



root = tk.Tk()

def callback(a,b,c):
    c = code.get()
    e4.config(bg='red')
    if c.isdigit():
        if len(c) == 10:
            e4.config(bg='green')
        elif len(c) > 10:
            code.set(c[:10])
            e4
    elif len(c) > 10:
        code.set(c[:10])

def srch():
    file = open('names.txt', 'r')
    top = tk.Toplevel()
    top.geometry(f'{root.winfo_width()}x{root.winfo_height()}')
    text = tk.Text(top)
    text.grid(row=0, column=0)
    for l in file:
        if search.get() in l:
            text.insert(tk.INSERT, l)


def register():
    reg.register(
        name.get(),
        last.get(),
        birth.get(),
        code.get(),
    )



l1 = tk.Label(root, text='Name')
l1.grid(row=0 , column=0)

l2 = tk.Label(root, text='Last Name')
l2.grid(row=1 , column=0)

l3 = tk.Label(root, text='Birth Date')
l3.grid(row=2 , column=0)

l4 = tk.Label(root, text='ID Code')
l4.grid(row=3 , column=0)



name = tk.StringVar()
e1 = tk.Entry(root, textvariable=name)
e1.grid(row=0, column=1)

last = tk.StringVar()
e2 = tk.Entry(root, textvariable=last)
e2.grid(row=1, column=1 )

birth = tk.StringVar()
e3 = tk.Entry(root, textvariable=birth)
e3.grid(row=2, column=1 )

code = tk.StringVar()
code.trace('w', callback)
e4 = tk.Entry(root, textvariable=code)
e4.grid(row=3, column=1 )


frame = tk.Frame()
frame.grid(row=4, column=0, columnspan=2)


b1= tk.Button(frame, text='regester', command=register)
b1.grid(row=4, column=0)

b2= tk.Button(frame, text='cancle', command=root.destroy)
b2.grid(row=4, column=1)

ttk.Separator(root,orient=tk.HORIZONTAL).grid(row=5, column=0, columnspan=2, sticky='ew')

tk.Label(root, text='Search').grid(row=6, column=0)
search = tk.Entry(root)
search.grid(row=6, column=1)
tk.Button(root, text='Search',command=srch).grid(row=7, column=0, columnspan=2)


root.mainloop()