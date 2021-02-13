import tkinter as tk


root = tk.Tk()

spin = tk.Spinbox(root, from_ =0, to=9, wrap=True )
spin.pack()

root.mainloop()