"""
File: koch.py
Date: 10/7/2018
Author: Jake Cariello (jec91)
Purpose: Uses Turtle Graphics to draw a Koch Curve (one-sided Koch Snowflake)
         For info, see: https://en.wikipedia.org/wiki/Koch_snowflake

Duke Community Standard:
I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: jec91
"""

# %% Imports
import turtle

# %% Define functions

# fcn for "bouncing" a value within the range [0, 255]
# using it for the red value
value = 255
step = -5


def next_value():
    # need to declare these vars as "global" so that they may be mutated w/in the fcn
    global value
    global step

    value += step

    if value in [0, 255]:
        step *= -1

    print(value)
    return value


def koch_curve(t, length, lvl=0):
    if lvl == 0:
        t.forward(length)
    else:
        koch_curve(t, length / 3, lvl - 1)
        for angle in [60, 240, 60]:
            t.left(angle)
            next_color_val = next_value()
            t.pencolor(255, next_color_val, next_color_val)
            koch_curve(t, length / 3, lvl - 1)


def init_turtle(t):
    t.pensize(2)
    t.speed(0)
    t.pencolor(255, 255, 255)

    kasa.penup()
    kasa.setposition(-300, 0)
    kasa.pendown()


# %% Main code if script is run
if __name__ == '__main__':
    wn = turtle.Screen()
    wn.clearscreen()
    wn.colormode(255)
    wn.bgcolor('black')

    try:
        kasa = turtle.Turtle()
    except:  # I am aware that this is "too broad," but it does the trick
        kasa = turtle.Turtle()

    init_turtle(kasa)

    koch_curve(kasa, 600, 4)

    from sys import platform

    if platform == 'win32':
        wn.exitonclick()
