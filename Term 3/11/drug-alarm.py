import tkinter as tk
import tkinter.ttk as ttk
from time import sleep
from threading import Thread

##################################def trace
def callback1(a, b, c):
    n_1.set(name1.get())

def callback2(a, b, c):
    n_2.set(name2.get())

def callback3(a, b, c):
    n_3.set(name3.get())

##########################

def callback_t_1(a, b, c):
    h1 = int(h_p_1.get())
    m1 = int(m_p_1.get())
    s1 = int(s_p_1.get())
    t_1.set('%02d:%02d:%02d'%(h1, m1, s1))


def callback_t_2(a, b, c):
    h2 = int(h_p_2.get())
    m2 = int(m_p_2.get())
    s2 = int(s_p_2.get())
    t_2.set('%02d:%02d:%02d'%(h2, m2, s2))

def callback_t_3(a, b, c):
    h3 = int(h_p_3.get())
    m3 = int(m_p_3.get())
    s3 = int(s_p_3.get())
    t_3.set('%02d:%02d:%02d'%(h3, m3, s3))
###################

def time_format(seconds):
    h = int(seconds/3600)
    tem = seconds%3600
    m = tem/60
    s = tem%60
    return'%02d:%02d:%02d'%(h, m, s)

def counter(seconds, var, button):
    button.config(state=tk.DISABLED)
    while seconds:
        sleep(1)
        seconds -=1
        var.set(time_format(seconds))
    button.config(state=tk.ACTIVE)

def start(number):
    if number==1:
        seconds1 =int(h_p_1.get())*3600 + int(m_p_1.get())*60 + int(s_p_1.get())
        th1 = Thread(target=counter, args=(seconds1, t_1, b1))
        th1.start()
    elif number==2:
        seconds2 =int(h_p_2.get())*3600 + int(m_p_2.get())*60 + int(s_p_2.get())
        th2 = Thread(target=counter, args=(seconds2, t_2, b2))
        th2.start()
    else:
        seconds3 =int(h_p_3.get())*3600 + int(m_p_3.get())*60 + int(s_p_3.get())
        th3 = Thread(target=counter, args=(seconds3, t_3, b3))
        th3.start()
#########################################
root = tk.Tk()

note = ttk.Notebook(root)
note.grid(row=0, column=0)

patients = ttk.Frame(note)
note.add(patients, text='patients')

timers = ttk.Frame(note)
note.add(timers, text='timers')

###############################patient 1
lf1 = tk.LabelFrame(patients, text='Patient 1')
lf1.grid(row=0, column=0)

tk.Label(lf1, text='Name').grid(row=0, column=0)
tk.Label(lf1, text='Time').grid(row=1, column=0)

name1 = tk.StringVar()
name1.trace('w', callback1)
tk.Entry(lf1, textvariable=name1).grid(row=0, column=1)

######################################################Timer 1
t1 = tk.Frame(lf1)
t1.grid(row=1, column=1)

h_p_1 = tk.StringVar()
h_p_1.set("12")

m_p_1 = tk.StringVar()
m_p_1.set("30")

s_p_1 = tk.StringVar()
s_p_1.set("30")
tk.Spinbox(t1, textvariable=h_p_1, wrap=True, from_=0, to=23, state="readonly", width=2).grid(row=0, column=0)
tk.Spinbox(t1, textvariable=m_p_1, wrap=True, from_=0, to=59, state="readonly", width=2).grid(row=0, column=1)
tk.Spinbox(t1, textvariable=s_p_1, wrap=True, from_=0, to=59, state="readonly", width=2).grid(row=0, column=2)
#########################patient 2

lf2 = tk.LabelFrame(patients, text='patiens 2')
lf2.grid(row=2, column=0)

tk.Label(lf2, text='Name').grid(row=0, column=0)
tk.Label(lf2, text='Time').grid(row=1, column=0)

name2 = tk.StringVar()
name2.trace('w', callback2)
tk.Entry(lf2, textvariable=name2).grid(row=0, column=1)

######################################################Timer 2
t2 = tk.Frame(lf2)
t2.grid(row=1, column=1)

h_p_2 = tk.StringVar()
h_p_2.set("12")

m_p_2 = tk.StringVar()
m_p_2.set("30")

s_p_2 = tk.StringVar()
s_p_2.set("30")
tk.Spinbox(t2, textvariable=h_p_2, wrap=True, from_=0, to=23, state="readonly", width=2).grid(row=0, column=0)
tk.Spinbox(t2, textvariable=m_p_2, wrap=True, from_=0, to=59, state="readonly", width=2).grid(row=0, column=1)
tk.Spinbox(t2, textvariable=s_p_2, wrap=True, from_=0, to=59, state="readonly", width=2).grid(row=0, column=2)
#########################patient 3

lf3 = tk.LabelFrame(patients, text='patiens 3')
lf3.grid(row=3, column=0)

tk.Label(lf3, text='Name').grid(row=0, column=0)
tk.Label(lf3, text='Time').grid(row=1, column=0)

name3 = tk.StringVar()
name3.trace('w', callback3)
tk.Entry(lf3, textvariable=name3).grid(row=0, column=1)

###########################################################Timer 3
t3 = tk.Frame(lf3)
t3.grid(row=1, column=1)

h_p_3 = tk.StringVar()
h_p_3.set("12")

m_p_3 = tk.StringVar()
m_p_3.set("30")

s_p_3 = tk.StringVar()
s_p_3.set("30")
tk.Spinbox(t3, textvariable=h_p_3, wrap=True, from_=0, to=23, state="readonly", width=2).grid(row=0, column=0)
tk.Spinbox(t3, textvariable=m_p_3, wrap=True, from_=0, to=59, state="readonly", width=2).grid(row=0, column=1)
tk.Spinbox(t3, textvariable=s_p_3, wrap=True, from_=0, to=59, state="readonly", width=2).grid(row=0, column=2)

######################################################## The first row of timer
n_1 = tk.StringVar()
n_1.set('patient 1')
tk.Label(timers, textvariable=n_1).grid(row=0, column=0, padx=10, pady=10)
###############
n_2 = tk.StringVar()
n_2.set('patient 2')
tk.Label(timers, textvariable=n_2).grid(row=0, column=1, padx=10, pady=10)
################
n_3 = tk.StringVar()
n_3.set('patient 3')
tk.Label(timers, textvariable=n_3).grid(row=0, column=2, padx=10, pady=10)
######################################################## The second row of timer
t_1 = tk.StringVar()
t_1.set('00:00:00')
tk.Label(timers, textvariable=t_1).grid(row=1, column=0)
################
t_2 = tk.StringVar()
t_2.set('00:00:00')
tk.Label(timers, textvariable=t_2).grid(row=1, column=1)
################
t_3 = tk.StringVar()
t_3.set('00:00:00')
tk.Label(timers, textvariable=t_3).grid(row=1, column=2)
######################################################## The third row of timer
b1 = tk.Button(timers, text='Start', command= lambda: start(1))
b1.grid(row=2, column=0)

b2 = tk.Button(timers, text='Start', command= lambda: start(2))
b2.grid(row=2, column=1)

b3 = tk.Button(timers, text='Start', command= lambda: start(3))
b3.grid(row=2, column=2)
######################################################## The forth row of timer
tk.Button(timers, text='Cancel', command=root.destroy).grid(row=3, column=0, columnspan=3)
############################################################
h_p_1.trace('w',callback_t_1)
m_p_1.trace('w',callback_t_1)
s_p_1.trace('w',callback_t_1)

h_p_2.trace('w',callback_t_2)
m_p_2.trace('w',callback_t_2)
s_p_2.trace('w',callback_t_2)

h_p_3.trace('w',callback_t_3)
m_p_3.trace('w',callback_t_3)
s_p_3.trace('w',callback_t_3)

root.mainloop()