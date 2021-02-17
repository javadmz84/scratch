import tkinter as tk

col = {
    '0': 'black',
    '1': 'brown',
    '2': 'red',
    '3': 'orange',
    '4': 'yellow',
    '5': 'green',
    '6': 'blue',
    '7': 'purple',
    '8': 'gray',
    '9': 'white',
}

def cal():
    val = spin1.get() + spin2.get() + int(spin3.get())*'0'+'ohm'
    label.config(text=val)

    spin1.config(bg=col[spin1.get()])
    spin2.config(bg=col[spin2.get()])
    spin3.config(bg=col[spin3.get()])

root = tk.Tk()
spin_cnf = {
    'from_':0,
    'to':9,
    'wrap':True,
    'width':5,
    'font':('times', 20)
}
label = tk.Label(root, text='', font=('times', 20))
label.pack()
frame = tk.Frame(root)
frame.pack()
spin1 = tk.Spinbox(root, cnf=spin_cnf)
spin1.pack(side=tk.LEFT)
spin2 = tk.Spinbox(root, cnf=spin_cnf)
spin2.pack(side=tk.LEFT)
spin3 = tk.Spinbox(root, cnf=spin_cnf)
spin3.pack(side=tk.LEFT)

b = tk.Button(root, text='Calculate',command=cal  ,font=('times',20))
b.pack()
root.mainloop()
