import tkinter as tk
import tkinter.ttk as ttk

# from databse import functions

def register_passnger():
    pass

# Main Frames
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
register_notebook.add(tab_register_person, text='Flight')
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

################ Register Passenger
tk.Label(tab_register_person, text='Fullname').grid(row=0, column=0)
person_fullname_register = tk.StringVar()
tk.Entry(tab_register_person, textvariable=person_fullname_register).grid(row=0, column=1)

tk.Label(tab_register_person, text='ID Number').grid(row=1, column=0)
person_id_number_register = tk.StringVar()
tk.Entry(tab_register_person, textvariable=person_id_number_register).grid(row=1, column=1)

tk.Button(tab_register_person, text='Register'. command=register_passnger).grid(row=2, column=1)


root.mainloop()