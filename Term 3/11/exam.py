import tkinter as tk

def up():
    global temp
    temp += 1
    fan()

def down():
    global temp
    temp -= 1
    fan()

def fan():
    temperature.set('Temperature: ' + str(temp))
    if temp >=30:
        fan_state.set('Fan is on')
        label2['background'] = 'green'
    else:
        fan_state.set('Fan is off')
        label2['background'] = 'red'

root = tk.Tk()
root.geometry('300x150')
temp = 25
temperature = tk.StringVar()
fan_state = tk.StringVar()
button1 = tk.Button(root, text = '⏶', command = up)
button2 = tk.Button(root, text='⏷', command = down)
label1 = tk.Label(root, textvariable=temperature)
label2 = tk.Label(root, textvariable =fan_state)
button1.pack()
label1.pack()
button2.pack()
label2.pack()
root.mainloop()