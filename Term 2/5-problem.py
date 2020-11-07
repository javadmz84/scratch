import turtle as tr
import random as rnd


tr.speed(1000)
for j in range(100):
    tr.penup()
    x_position = rnd.randint(-400, 300)
    y_position = rnd.randint(-250, 200)
    tr.goto(x_position, y_position)
    tr.pendown()
    pen_size = rnd.randint(1, 5)
    tr.pensize(pen_size)
    for i in range(4):
        tr.fd(150)
        tr.lt(90)
tr.done()
    
    