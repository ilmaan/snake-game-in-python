import turtle as t
import random as rd
import time as ti

def inside_window():
    leftlim = (-t.window_width() / 2) + 100
    rightlim = (t.window_width() / 2) - 100
    toplim = (t.window_height() / 2) - 100
    bottomlim = (-t.window_height() / 2) + 100
    (x,y) = t.pos()
    inside = leftlim < x < rightlim and bottomlim < y < toplim
    return inside

def move():
    if inside_window():
        angle = rd.randint(1,180)
        dist = rd.randint(1,100)
        t.right(angle)
        t.forward(dist)

    else:
        t.backward(200)    


t.shape('turtle')
t.fillcolor('green')
t.bgcolor('black')
t.speed(2)

while True:
    move()






