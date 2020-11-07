import turtle as tr
import random as rnd


pen_size = rnd.randint(1, 5)
tr.pensize(pen_size)
for i in range(3):
    tr.fd(150)
    tr.lt(120)

tr.done()