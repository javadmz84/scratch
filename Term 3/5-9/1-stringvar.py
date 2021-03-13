from tkcalendar import DateEntry
import tkinter as tk
import reg
import tkinter.ttk as ttk







def alphabet(a,b,c):
    if name.get().isalpha():
        e1.config(bg='green')
    else:
        e1.config(bg='red')

def alphabetl(a,b,c):
    if last.get().isalpha():
        e2.config(bg='green')
    else:
        e2.config(bg='red')
        


def callback(a,b,c):
    c = code.get()
    e4.config(bg='red')
    if c.isdigit():
        if len(c) == 10:
            e4.config(bg='green')
        elif len(c) > 10:
            code.set(c[:10])
            e4.config(bg='green')
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


def register(a=None):
    reg.register(
        name.get(),
        last.get(),
        e3.get(),
        code.get(),
    )
    name.set('')
    last.set('')
    code.set('')
    e1.config(bg='white')
    e2.config(bg='white')
    e4.config(bg='white')

root = tk.Tk()
root.bind('<Return>', register)

l1 = tk.Label(root, text='Name')
l1.grid(row=0 , column=0)

l2 = tk.Label(root, text='Last Name')
l2.grid(row=1 , column=0)

l3 = tk.Label(root, text='Birth Date')
l3.grid(row=2 , column=0)

l4 = tk.Label(root, text='ID Code')
l4.grid(row=3 , column=0)



name = tk.StringVar()
name.trace('w', alphabet)

e1 = tk.Entry(root, textvariable=name)
e1.grid(row=0, column=1)

last = tk.StringVar()
last.trace('w', alphabetl)

e2 = tk.Entry(root, textvariable=last)
e2.grid(row=1, column=1 )




e3 = DateEntry(root, width=12, background='darkblue', foreground='white',
    borderwidth=2, date_pattern='y-mm-dd')
e3.grid(row=2, column=1, sticky='we' )

code = tk.StringVar()
code.trace('w', callback)
e4 = tk.Entry(root, textvariable=code)
e4.grid(row=3, column=1 )


frame = tk.Frame()
frame.grid(row=4, column=0, columnspan=2)


tk.Button(frame, text='regester', command=register).grid(row=4, column=0)

tk.Button(frame, text='cancle', command=root.destroy).grid(row=4, column=1)

ttk.Separator(root,orient=tk.HORIZONTAL).grid(row=5, column=0, columnspan=2, sticky='ew')

tk.Label(root, text='Search').grid(row=6, column=0)
search = tk.Entry(root)
search.grid(row=6, column=1)
tk.Button(root, text='Search',command=srch).grid(row=7, column=0, columnspan=2)


root.mainloop()