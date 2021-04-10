import tkinter as tk
import tkinter.ttk as ttk


root = tk.Tk()

note = ttk.Notebook(root)
note.grid(row=0, column=0)
#####################################3
patients = ttk.Frame(note)
note.add(patients, text='Patients')
timers = ttk.Frame(note)
note.add(timers, text='Timers')
##########################################
lf1 = tk.LabelFrame(patients, text='Patient 1')
lf1.grid(row=0, column=0)

tk.Label(lf1, text='Name').grid(row=0, column=0)
tk.Label(lf1, text='Tiime').grid(row=1, column=0)
name1 = tk.StringVar()
time1 = tk.StringVar()
tk.Entry(lf1, textvariable=name1).grid(row=0, column=1)
tk.Entry(lf1, textvariable=time1).grid(row=1, column=1)
#####################second row of patient####################
lf2 = tk.LabelFrame(patients, text='Patient 2')
lf2.grid(row=1, column=0)
tk.Label(lf2, text='Name').grid(row=0, column=0)
tk.Label(lf2, text='Time').grid(row=1, column=0)
name2 = tk.StringVar()
time2 = tk.StringVar()

tk.Entry(lf2, textvariable=name2).grid(row=0, column=1)
tk.Entry(lf2, texrvariable=time2).grid(row=1, column=1)
##################Third row of patients#############
lf3 = tk.LabelFrame(patients, text='Patient 3')
lf3.grid(row=2, column=0)
tk.Label(lf3, text='Name').grid(row=0, column=0)
tk.Label(lf3, text='Time').grid(row=1, column=0)
name3 = tk.StringVar()
time3 = tk.StringVar()
#####################################
tk.Entry(lf3, textvariable=name3).grid(row=0, column=1)
tk.Entry(lf3, textvariable=time3).grid(row=1, column=1)


##########################################
root.mainloop()