import tkinter as tk
import reg


root = tk.Tk()

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

name = tk.Entry(root)
name.grid(row=0, column=1 )

last = tk.Entry(root)
last.grid(row=1, column=1 )

birth = tk.Entry(root)
birth.grid(row=2, column=1 )

code = tk.Entry(root)
code.grid(row=3, column=1 )

frame = tk.Frame()
frame.grid(row=4, column=0, columnspan=2)


b1= tk.Button(frame, text='regester', command=register)
b1.grid(row=4, column=0)

b2= tk.Button(frame, text='cancle', command=root.destroy)
b2.grid(row=4, column=1)





root.mainloop()