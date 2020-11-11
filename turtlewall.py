import turtle as t
import time as ti
from itertools import cycle

colors = cycle(['red','white','yellow','green','blue','grey','purple','pink','brown','orange','violet'])

def circle(size,angle,forw):
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(forw)
    circle(size+1,angle+1,forw+5)

s = int(input("enter size"))
a = int(input("enter angle"))
f = int(input("enter distance"))
t.bgcolor("black")
t.speed(9)
t.pensize(2)
circle(s,180,1)
ti.sleep(5)
t.hideturtle()

