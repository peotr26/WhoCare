from turtle import *
from random import randrange

colormode(255)
ht()
speed(0)

def goto_am(w, h):
    up()
    goto(w, h)

def next_line(s, o):
    up()
    move(s,o+180)
    move(4,o+90)
    down()

def move(s, o):
    up()
    setheading(0)
    forward(s)

def pixel(colour):
    down()
    begin_fill()
    color(colour)
    for i in range(0,4):
        forward(4)
        left(90)
    end_fill()

def choose_colour():
    return randrange(0, 256, 50), randrange(0, 256, 50), randrange(0, 256, 50)

def line(s, o):
    for i in range(0,s):
        pixel(choose_colour())
        move(4, o)
        #print('b')

def display():
    goto_am(-(window_width()/2), -(window_height()/2))
    start_height = -(window_height()/2)
    for i in range(0, window_height()):
        line(int(window_width()/4), 0)
        print('a')
        goto_am(-(window_width()/2), start_height+(i*4))

display()
mainloop()
