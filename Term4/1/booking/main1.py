import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
from database import functions

def back():
    destroy_all()
    root.deiconify()
    tree_view_passenger_update()


def destroy_all():
    for widget in root.winfo_children():
        if isinstance(widget, tk.Toplevel):
            widget.destroy()


def update_passenger(id, fullname, idnumber):
    functions.update_person(fullname, idnumber, id)
    back()


def delete_passenger(id):
    answer = tk.messagebox.askyesno(title='Warning', message='Are you sure?')
    if answer:
        functions.delete_person(id)
    back()

def passenger_search(a,b,c):
    tree_view_passenger_update(filter=True)


def item_selected(event):
    for selected_item in tree_view_passengers.selection():
        item = tree_view_passengers.item(selected_item)
        record = item['values']
    if record:
        root.withdraw()
        top = tk.Toplevel()
        frame_update = tk.Frame(top)
        frame_update.grid(row=0, column=0, padx=(5, 5), pady=(5, 5))

        tk.Label(frame_update, text='ID').grid(row=0, column=0)
        person_id_update = tk.StringVar()
        person_id_update.set(record[0])
        tk.Entry(frame_update, textvariable=person_id_update, state='readonly').grid(row=0, column=1)

        tk.Label(frame_update, text='FullName').grid(row=1, column=0)
        person_fullname_update = tk.StringVar()
        person_fullname_update.set(record[1])
        tk.Entry(frame_update, textvariable=person_fullname_update).grid(row=1, column=1)

        tk.Label(frame_update, text='ID Number').grid(row=2, column=0)
        person_id_number_update = tk.StringVar()
        person_id_number_update.set(record[2])
        tk.Entry(frame_update, textvariable=person_id_number_update).grid(row=2, column=1)

        update = lambda : update_passenger(
            record[0], person_fullname_update.get(), person_id_number_update.get()
        )
        delete = lambda : delete_passenger(record[0])

        tk.Button(frame_update, text='Update', command=update).grid(row=2, column=0)
        tk.Button(frame_update, text='Delete', command=delete).grid(row=3, column=0)

def tree_view_passenger_update(filter=False):
    tree_view_passengers.delete(*tree_view_passengers.get_children())
    passengers = []
    if not filter:
        l = functions.passenger_list()
    else:
        l = functions.passenger_filter(person_id_number_search.get())
    for row in l:
        passengers.append((f'{row[0]}', f'{row[1]}', f'{row[2]}'))

    for passenger in passengers:
        tree_view_passengers.insert('', tk.END, values=passenger)



def register_passnger():
    functions.insert_person(
        person_fullname_register.get(),
        person_id_number_register.get()
    )
    person_fullname_register.set(''),
    person_id_number_register.set('')
    tree_view_passenger_update()

############################ Main Frames
root = tk.Tk()
left_frame = tk.Frame(root)
right_frame = tk.Frame(root)

left_frame.grid(row=0, column=0, padx=(5, 5), pady=(5, 5))
right_frame.grid(row=0, column=1, padx=(0, 5), pady=(5, 5))

############### Rigister Notebook
register_notebook = ttk.Notebook(left_frame)
tab_register_person = ttk.Frame(register_notebook)
tab_set_flight = ttk.Frame(register_notebook)
tab_book_ticket = ttk.Frame(register_notebook)
register_notebook.add(tab_register_person, text='Passnger')
register_notebook.add(tab_set_flight, text='Flight')
register_notebook.add(tab_book_ticket, text='ticket')
register_notebook.grid(row=0, column=0)

################### Right Notebook
right_notebook = ttk.Notebook(right_frame)
passengers = ttk.Frame(right_notebook)
flights = ttk.Frame(right_notebook)
tickets = ttk.Frame(right_notebook)
right_notebook.add(passengers, text='Passangers')
right_notebook.add(flights, text='Flights')
right_notebook.add(tickets, text='Tickets')
right_notebook.grid(row=0, column=0)

################ Left Register Passenger
tk.Label(tab_register_person, text='Fullname').grid(row=0, column=0)
person_fullname_register = tk.StringVar()
tk.Entry(tab_register_person, textvariable=person_fullname_register).grid(row=0, column=1)
tk.Label(tab_register_person, text='ID Number').grid(row=1, column=0)
person_fullname_register = tk.StringVar()
tk.Entry(tab_register_person, textvariable=person_fullname_register).grid(row=0, column=1)

tk.Label(tab_register_person, text='ID Number').grid(row=1, column=0)
person_id_number_register = tk.StringVar()
tk.Entry(tab_register_person, textvariable=person_id_number_register).grid(row=1, column=1)

tk.Button(tab_register_person, text='Registor', command=register_passnger).grid(row=2, column=1)
################  Passenger List
tk.Label(passengers, text='Query').grid(row=0, column=0)
person_id_number_search = tk.StringVar()
person_id_number_search.trace('w', passenger_search)
tk.Entry(passengers, textvariable=person_id_number_search).grid(row=0, column=1)
# tk.Button(passengers, text='Passengers   List', command=tree_view_passenger_update).grid(row=0, column=2)

columns = ('#1', '#2', '#3')
tree_view_passengers = ttk.Treeview(passengers, columns=columns, show='headings')
tree_view_passengers.heading('#1', tex='PSG ID')
tree_view_passengers.column('#1', anchor=tk.CENTER, stretch=tk.NO, width=60)
tree_view_passengers.heading('#2', text='FullName')
tree_view_passengers.heading('#3', text='ID Number')
tree_view_passengers.column('#3', anchor=tk.CENTER, stretch=tk.NO)
tree_view_passengers.bind("<<TreeviewSelect>>", item_selected)
tree_view_passengers.grid(row=1, column=0, columnspan=3, sticky='nsew')
scrollbar = ttk.Scrollbar(passengers,orient=tk.VERTICAL, command=tree_view_passengers.yview)
tree_view_passengers.configure(yscroll=scrollbar.set)
scrollbar.grid(row=1, column=3, sticky='ns')
tree_view_passenger_update()

root.mainloop()