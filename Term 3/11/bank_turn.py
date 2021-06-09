from tkinter import *
from datetime import datetime

###############functions#############

def press(label):
    global counter_list
    if counter_list:
        con[label]["textvariable"].set(counter_list.pop(0))


def get_date():
    dt = datetime.now()
    return dt.strftime('%d %b %Y')

def get_time():
    dt = datetime.now()
    return dt.strftime('%H:%M:%S')

def get_number():
    global counter, counter_list
    counter +=1
    counter_list.append(counter)
    con["date"]["textvariable"].set(get_date())
    con["time"]["textvariable"].set(get_time())
    con["number"]["textvariable"].set('You turn {}'.format(counter))
    con["waiting"]["textvariable"].set('Waiting {}'.format(len(counter_list)))
    

counter = 0
counter_list = list()
root = Tk()

con = {
    'turn':{
        'text': 'Get a number',
        'width': 10,
        'height': 5,
        'bg': '#FF82A9'
    },
    'cancel':{
        'text': 'Cancel',
        'width': 10,
        'height': 5,
        'bg': '#ff8585'
    },
    'date':{
        'textvariable': StringVar(),
        'font': ('Courier', 14)
    },
    'time':{
        'textvariable': StringVar(),
        'font': ('Courier', 14)
    },
    'number':{
        'textvariable': StringVar(),
        'font': ('Courier', 14)
    },
    'waiting':{
        'textvariable': StringVar(),
        'font': ('Courier',14)
    },
    'op1':{
        'text': 'Operator1',
        'bg':'#f06966',
        'height': 5,
        'width':15
    },
    'op2':{
        'text': 'Operator2',
        'bg':'#f06966',
        'height': 5,
        'width':15
    },
    'op3':{
        'text': 'Operator3',
        'bg':'#f06966',
        'height': 5,
        'width':15
    },
    'lop1':{
        "textvariable": StringVar(),
        "bg": "green",
        "height":5,
        "width":10
    },
    'lop2':{
        "textvariable": StringVar(),
        "bg": "green",
        "height":5,
        "width":10
    },
    'lop3':{
        "textvariable": StringVar(),
        "bg": "green",
        "height":5,
        "width":10
    }
}

root.title("Main")
root.geometry("200x270")
root.resizable(0, 0)
root.configure(bg='#7F95D1')

Button(root, command=get_number, cnf= con['turn']).grid(row=0, column=0, padx=45)
Button(root, command=root.destroy, cnf=con['cancel']).grid(row=1, column=0, padx=45)

operators = Toplevel()
operators.title("Operators")
operators.geometry("600x200")
operators.resizable(0, 0)
operators.configure(bg='#f1ac9d')
Button(operators, cnf=con['op1'], command= lambda: press('lop1')).grid(row=0, column=0, padx=25, pady=10)
Button(operators, cnf=con['op2'], command= lambda: press('lop2')).grid(row=0, column=1, padx=25, pady=10)
Button(operators, cnf=con['op3'], command= lambda: press('lop3')).grid(row=0, column=2, padx=25, pady=10)
Label(operators, cnf=con['lop1']).grid(row=1, column=0, padx=25, pady=10)
Label(operators, cnf=con['lop2']).grid(row=1, column=1, padx=25, pady=10)
Label(operators, cnf=con['lop3']).grid(row=1, column=2, padx=25, pady=10)

customers = Toplevel()
customers.title("customers")
customers.geometry("200x200")
customers.resizable(0, 0)
Label(customers, cnf=con['date']).grid(row=0, column=0)
Label(customers, cnf=con['time']).grid(row=1, column=0)
Label(customers, cnf=con['number']).grid(row=2, column=0)
Label(customers, cnf=con['waiting']).grid(row=3, column=0)


root.mainloop()