from ttkwidgets.autocomplete import AutocompleteCombobox
from tkcalendar import DateEntry
import pandas as pd
import json
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
from database import functions

def find_flight(a, b, c):
    v = functions.find_flight(flight_ticket.get())
    for f in v:
        flight_ticket_label.set(f'{f[1]} {f[2]}')


def find_passenger(a, b, v):
    v = functions.find_passenger(passenger_ticket.get())
    for p in v:
        passenger_ticket_label.set(f'{p[1]} {p[2]}')


def flight_search(a,b,c):
    treeview_flight_update(filter=True)

def treeview_flight_update(filter=False):
    tree_view_flights.delete(*tree_view_flights.get_children())
    flughts = []
    if not filter:
        l = functions.flight_list()
    else:
        l = functions.flight_filter(flight_id_search.get())
    for row in l:
        flughts.append((f"{row[0]}", f"{row[1]}", f"{row[2]}", f"{row[3]}", f"{row[4]}", f"{row[5]}", f"{row[6]}", f"{row[7]}" ))
    for flight in flughts:
        tree_view_flights.insert("", tk.END, values=flight)


def book_flight():
    functions.set_flight(
        flight_from_city_set.get(),
        flight_to_city_set.get(),
        flight_depratur_set.get(),
        flight_arrival_set.get(),
        flight_agency_set.get(),
        flight_seats_set.get(),
        flight_price_set.get(),
    )
    flight_from_city_set.set(""),
    flight_to_city_set.set(""),
    flight_agency_set.set(""),
    flight_seats_set.set(0),
    flight_price_set.set(0),
    treeview_flight_update()
def read_air_ports(add):
    df = pd.DataFrame(json.load(open(add, 'r', encoding='utf-8')))
    return df['iata'].to_list()

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
tree_view_passengers.column('#3', anchor=tk.CENTER, stretch=tk.NO)
tree_view_passengers.bind("<<TreeviewSelect>>", item_selected)
tree_view_passengers.grid(row=1, column=0, columnspan=3, sticky='nsew')
scrollbar = ttk.Scrollbar(passengers,orient=tk.VERTICAL, command=tree_view_passengers.yview)
tree_view_passengers.configure(yscroll=scrollbar.set)
scrollbar.grid(row=1, column=3, sticky='ns')
tree_view_passenger_update()
################################

#################################
airports = read_air_ports('airports.json')
tk.Label(tab_set_flight, text="From").grid(row=0, column=0)
flight_from_city_set = tk.StringVar()
AutocompleteCombobox(
    tab_set_flight,
    textvariable=flight_from_city_set,
    completevalues=airports).grid(row=0, column=1)

tk.Label(tab_set_flight, text="To").grid(row=1, column=0)
flight_to_city_set = tk.StringVar()
AutocompleteCombobox(

    tab_set_flight,
    textvariable=flight_to_city_set,
    completevalues=airports).grid(row=1, column=1)

tk.Label(tab_set_flight, text="Depratur").grid(row=2, column=0)
flight_depratur_set = tk.StringVar()
DateEntry(tab_set_flight, date_pattern='y-mm-dd' ,textvariable=flight_depratur_set, year=2021).grid(row=2, column=1)

tk.Label(tab_set_flight, text="Arrival").grid(row=3, column=0)
flight_arrival_set = tk.StringVar()
DateEntry(tab_set_flight, date_pattern='y-mm-dd', textvariable=flight_arrival_set, year=2021).grid(row=3, column=1)

agencies = ['jafar', 'mahan', 'qehsm', 'iran-air']
tk.Label(tab_set_flight, text="Agency").grid(row=4, column=0)
flight_agency_set = tk.StringVar()
AutocompleteCombobox(

    tab_set_flight,
    textvariable=flight_agency_set,
    completevalues=agencies).grid(row=4, column=1)

tk.Label(tab_set_flight, text="Seats").grid(row=5, column=0)
flight_seats_set = tk.IntVar()
tk.Entry(tab_set_flight, textvariable=flight_seats_set).grid(row=5, column=1)

tk.Label(tab_set_flight, text="Price").grid(row=6, column=0)
flight_price_set = tk.IntVar()
tk.Entry(tab_set_flight, textvariable=flight_price_set).grid(row=6, column=1)

tk.Button(tab_set_flight, text="Registor", command=book_flight).grid(row=7, column=1)

######################flight list
tk.Label(flights, text="Query").grid(row=0, column=0)
flight_id_search = tk.StringVar()
# flight_id_search.trace('w', passenger_search)
tk.Entry(flights, textvariable=flight_id_search).grid(row=0, column=1)

columns = ("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8")
tree_view_flights = ttk.Treeview(flights, columns=columns, show="headings")
tree_view_flights.heading("#1", text="FLT ID")
tree_view_flights.column("#1", anchor=tk.CENTER, stretch=tk.NO, width=50)
tree_view_flights.heading("#2", text="From")
tree_view_flights.column("#2", anchor=tk.CENTER, stretch=tk.NO, width=50)
tree_view_flights.heading("#3", text="To")
tree_view_flights.column("#3", anchor=tk.CENTER, stretch=tk.NO, width=50)
tree_view_flights.heading("#4", text="Dep")
tree_view_flights.column("#4", anchor=tk.CENTER, stretch=tk.NO, width=100)
tree_view_flights.heading("#5", text="Arr")
tree_view_flights.column("#5", anchor=tk.CENTER, stretch=tk.NO, width=100)
tree_view_flights.heading("#6", text="Age")
tree_view_flights.column("#6", anchor=tk.CENTER, stretch=tk.NO, width=100)
tree_view_flights.heading("#7", text="Tot")
tree_view_flights.column("#7", anchor=tk.CENTER, stretch=tk.NO, width=50)
tree_view_flights.heading("#8", text="$")
tree_view_flights.column("#8", anchor=tk.CENTER, stretch=tk.NO, width=50)
# tree_view_flights.bind("<<TreeviewSelect>>", item_selected)
tree_view_flights.grid(row=1, column=0, columnspan=3, sticky="nsew")
scrollbar = ttk.Scrollbar(flights, orient=tk.VERTICAL, command=tree_view_flights.yview)
tree_view_flights.configure(yscroll=scrollbar.set)
scrollbar.grid(row=1, column=3, sticky="ns")
treeview_flight_update()

###############################
passenger_ticket_label = tk.StringVar()
tk.Label(tab_book_ticket, textvariable=passenger_ticket_label).grid(row=0, column=0, columnspan=2)
tk.Label(tab_book_ticket, text='Passenger').grid(row=1, column=0)
passenger_ticket = tk.StringVar()
passenger_ticket.trace('w', find_passenger)
tk.Entry(tab_book_ticket, textvariable=passenger_ticket).grid(row=1, column=1)


flight_ticket_label = tk.StringVar()
tk.Label(tab_book_ticket, textvariable=flight_ticket_label).grid(row=2, column=0, columnspan=2)
tk.Label(tab_book_ticket, text='Flight').grid(row=3, column=0)
flight_ticket= tk.StringVar()
flight_ticket.trace('w', find_flight)
tk.Entry(tab_book_ticket, textvariable=flight_ticket).grid(row=3, column=1)

tk.Button(tab_book_ticket, text='Set Ticket').grid(row=4, column=0)

root.mainloop()