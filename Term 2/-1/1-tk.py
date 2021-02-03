import tkinter as tk


def press():
    print(e1.get())

# widget (Label, Entry, Button)
root = tk.Tk()
L1 = tk.Label(root, text="Ajisa is coming!")
L1.pack()
e1 = tk.Entry(root)
e1.pack()
b1 = tk.Button(root, text="press me!", command=press)
b1.pack()
root.mainloop()
