from tkinter import *

root = Tk()

# ساخت تابع
def javad():
    mylabel = Label(root, text="کارت درسته")
    mylabel.pack()


# دکمه را ساختیم اما کاری انجام نمیدهد پس برایش تابع میسازیم که در بالا ساختیم
button = Button(root, text='click me',command=javad, fg='blue', bg='green')
button.pack()


root.mainloop()