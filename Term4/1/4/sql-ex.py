import tkinter as tk
import tkinter.ttk as ttk
import sqlalchemy as db



def register():
    query = db.insert(data). values(fullname=f"{fullname.get()}", idnum=f"{idnumber.get()}", phone=f"{phone.get()}")
    connection.execute(query)

def search():
    def update():
        query = db.update(data).values(
            fullname=search_fullname.get(),
            phone=search_phone.get(),
            ).where(data.c.idnum==res[0])
        connection.execute(query)

    def delete():
        query = db.delete(data).where(data.c.idnum ==res[0])
        connection.execute(query)
    top = tk.Toplevel()
    tk.Label(top, text='Full Name:').grid(row=0, column=0)
    tk.Label(top, text='Phone').grid(row=1, column=0)
    query = db.select(data).where(data.c.idnum==search_query.get())
    res = connection.execute(query)
    res = res.fetchone()

    search_fullname = tk.StringVar()
    search_fullname.set(res[1])
    tk.Entry(top, textvariable=search_fullname).grid(row=0, column=1)

    search_phone = tk.StringVar()
    search_phone.set(res[2])
    tk.Entry(top, textvariable=search_phone).grid(row=1, column=1)

    tk.Button(top, text='Update', command=update).grid(row=2, column=0)
    tk.Button(top, text='Delete', command=delete).grid(row=3, column=0)


engine = db.create_engine('mysql+pymysql://root:JaVaDmZ84!@localhost:3306/register')
connection = engine.connect()
metadata = db.MetaData()
data = db.Table("person", metadata, autoload=True, autoload_with=engine)

root = tk.Tk()

notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0)

frame1 = ttk.Frame(notebook, width=200, height=280)
frame2 = ttk.Frame(notebook, width=200, height=280)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

notebook.add(frame1, text='Register')
notebook.add(frame2, text='Search')

tk.Label(frame1, text='Full Name:').grid(row=0, column=0)
tk.Label(frame1, text='ID Num:').grid(row=1, column=0)
tk.Label(frame1, text='Phone').grid(row=2, column=0)

fullname = tk.StringVar()
tk.Entry(frame1, textvariable=fullname).grid(row=0, column=1)

idnumber = tk.StringVar()
tk.Entry(frame1, textvariable=idnumber).grid(row=1, column=1)

phone = tk.StringVar()
tk.Entry(frame1, textvariable=phone).grid(row=2, column=1)

tk.Button(frame1, text='Register', command=register).grid(row=3, column=0)
tk.Button(frame1, text='Cancle', command=root.destroy).grid(row=4, column=0)

# ############################################################################
tk.Label(frame2, text="Search:").grid(row=0, column=0)
search_query = tk.StringVar()
tk.Entry(frame2, textvariable=search_query).grid(row=0, column=1)
tk.Button(frame2, text='Search', command=search).grid(row=4, column=0)

root.mainloop()