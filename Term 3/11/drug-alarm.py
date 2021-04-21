import tkinter as tk  
import tkinter.ttk as ttk


###############functions#################
def callback1(a,b,c):
    p1.set(name1.get())

def callback2(a,b,c):
    p2.set(name2.get())

def callback3(a,b,c):
    p3.set(name3.get())

def time_format(seconds):
    h = int(seconds/3600)
    tem = h%3600
    m = int(tem/60)
    s = m%60
    return '%02d:%02d:%02d'(h, m, s)
        

root = tk.Tk()
note = ttk.Notebook(root)
note.grid(row=0, column=0)


patients = ttk.Frame(note)
note.add(patients, text='Patients')

timers= ttk.Frame(note)
note.add(timers, text='Timers')
##################First row of patients#################
lf1 = tk.LabelFrame(patients, text='Patient 1')
lf1.grid(row=0, column=0)
tk.Label(lf1, text='Name').grid(row=0, column=0)
tk.Label(lf1, text='Time').grid(row=1, column=0)
name1 = tk.StringVar()
time1 = tk.StringVar()
name1.trace('w',callback1)
tk.Entry(lf1, textvariable=name1).grid(row=0, column=1)
##################Timer 1###############
f1 = tk.Frame(lf1)
f1.grid(row=1, column=1)
h_p_l = tk.StringVar()
h_p_l.set('12')
m_p_l = tk.StringVar()
m_p_l.set('30')
s_p_l = tk.StringVar()
s_p_l.set('30')
tk.Spinbox(f1, from_=0, to=23, wrap=True, width=2, textvariable=h_p_l, state='readonly').grid(row=0, column=0)
tk.Spinbox(f1, from_=0, to=59, wrap=True, width=2, textvariable=m_p_l, state='readonly').grid(row=0, column=1)
tk.Spinbox(f1, from_=0, to=59, wrap=True, width=2, textvariable=s_p_l, state='readonly').grid(row=0, column=2)

##################Second row of patients###################
lf2 = tk.LabelFrame(patients, text='Patient 2')
lf2.grid(row=1, column=0)
tk.Label(lf2, text='Name').grid(row=0, column=0)
tk.Label(lf2, text='Time').grid(row=1, column=0)
name2 = tk.StringVar()
time2 = tk.StringVar()
name2.trace('w', callback2)
tk.Entry(lf2, textvariable=name2).grid(row=0, column=1)
##################Timer 2####################
f2 = tk.Frame(lf2)
f2.grid(row=1, column=1)
h_p_2 = tk.StringVar()
h_p_2.set('12')
m_p_2 = tk.StringVar()
m_p_2.set('30')
s_p_2 = tk.StringVar()
s_p_2.set('30')
tk.Spinbox(f2, from_=0, to=23, wrap=True, width=2, textvariable=h_p_2, state='readonly').grid(row=0, column=0)
tk.Spinbox(f2, from_=0, to=59, wrap=True, width=2, textvariable=m_p_2, state='readonly').grid(row=0, column=1)
tk.Spinbox(f2, from_=0, to=59, wrap=True, width=2, textvariable=s_p_2, state='readonly').grid(row=0, column=2)
##################Third row of patients###################
lf3 = tk.LabelFrame(patients, text='Patient 3')
lf3.grid(row=2, column=0)
tk.Label(lf3, text='Name').grid(row=0, column=0)
tk.Label(lf3, text='Time').grid(row=1, column=0)
name3 = tk.StringVar()
time3 = tk.StringVar()
name3.trace('w', callback3)
tk.Entry(lf3, textvariable=name3).grid(row=0, column=1)
#######
f3 = tk.Frame(lf3)
f3.grid(row=1, column=1)
h_p_3 = tk.StringVar()
h_p_3.set('12')
m_p_3 = tk.StringVar()
m_p_3.set('30')
s_p_3 = tk.StringVar()
s_p_3.set('30')
tk.Spinbox(f3, from_=0, to=23, wrap=True, width=2, textvariable=h_p_3, state='readonly').grid(row=0, column=0)
tk.Spinbox(f3, from_=0, to=59, wrap=True, width=2, textvariable=m_p_3, state='readonly').grid(row=0, column=1)
tk.Spinbox(f3, from_=0, to=59, wrap=True, width=2, textvariable=s_p_3, state='readonly').grid(row=0, column=2)

##############First row of timer##################
p1 = tk.StringVar()
p1.set('Patient1')
tk.Label(timers, textvariable=p1).grid(row=0, column=0, padx=10, pady=10)

p2 = tk.StringVar()
p2.set('Patient2')
tk.Label(timers, textvariable=p2).grid(row=0, column=1,  pady=10)
p3 = tk.StringVar()
p3.set('Patient3')
tk.Label(timers, textvariable=p3).grid(row=0, column=2, padx=10, pady=10)

##############The Second Row Of Timers#############
t1 = tk.StringVar()
t1.set('00:00:00')
tk.Label(timers, textvariable=t1).grid(row=1, column=0)

t2 = tk.StringVar()
t2.set('00:00:00')
tk.Label(timers, textvariable=t2).grid(row=1, column=1)

t3 = tk.StringVar()
t3.set('00:00:00')
tk.Label(timers, textvariable=t3).grid(row=1, column=2)

###############The Third Row Of Timers##############
b1 = tk.Button(timers, text='Start')
b1.grid(row=2, column=0)

b2 = tk.Button(timers, text='Start')
b2.grid(row=2, column=1)

b3 = tk.Button(timers, text='Start')
b3.grid(row=2, column=2)
#############the forth row of timer#############
tk.Button(timers, text='Cancel', command=root.destroy).grid(row=3, column=0, sticky=tk.E+tk.w, columnspan=3)
##################3
root.mainloop()