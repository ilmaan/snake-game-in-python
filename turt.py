import turtle as t
import time as ti
from itertools import cycle

colors = cycle(['red','white','yellow','green','blue','grey','purple','pink','brown','orange'])

def circle(size,angle,forw,shape):
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(forw)
    circle(size+3,angle+1,forw+5)

t.bgcolor("black")
t.speed(12)
t.pensize(2)
circle(30,10,1)
ti.sleep(5)
t.hideturtle()