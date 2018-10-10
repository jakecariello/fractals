"""
File: dragon.py
Date: 10/7/18
Author: Jake Cariello
Purpose: Uses Turtle Graphics to recursively draw a Dragon Curve
         For info, see: https://en.wikipedia.org/wiki/Dragon_curve
"""

import turtle
import time

# %% functions
def setup():
    try:
        franklin = turtle.Turtle()
    except:
        franklin = turtle.Turtle()

    franklin.speed(0)  # fastest setting

    franklin.penup()
    franklin.goto(0, -300)
    franklin.pendown()
    franklin.left(90)

    return franklin


def tree(t, length, lvl):

    if lvl == 0:
        t.forward(length)
    else:
        t.forward(length)
        t.left(45)
        tree(t, length / 2, lvl - 1)
        t.right(90)
        tree(t, length/ 2, lvl - 1)
        t.left(45)

    t.penup()
    t.back(length)
    t.pendown()


# %% testing code (only runs if this is main script)
if __name__ == '__main__':

    window = turtle.Screen()

    for k in range(0, 10):

        tree(setup(), 300, k)
        time.sleep(1)
