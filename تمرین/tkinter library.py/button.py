import tkinter as tk

root = tk.Tk()

# ساخت تابع
def javad():
    mylabel = tk.Label(root, text="کارت درسته")
    mylabel.pack()


# دکمه را ساختیم اما کاری انجام نمیدهد پس برایش تابع میسازیم که در بالا ساختیم
button = tk.Button(root, text='click me',command=javad, fg='blue', bg='green')
button.pack()
ll;kf;dls
root.mainloop()