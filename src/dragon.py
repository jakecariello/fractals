"""
File: dragon.py
Date: 10/7/18
Author: Jake Cariello
Purpose: Uses Turtle Graphics to recursively draw a Dragon Curve
         For info, see: https://en.wikipedia.org/wiki/Dragon_curve
"""

# %% imports
import turtle
import math as m

# %% functions
def setup():
    franklin = turtle.Turtle()

    franklin.speed(0)  # fastest setting

    franklin.penup()
    franklin.goto(300, 0)
    franklin.pendown()
    franklin.left(180)

    return franklin


def dragon(t, length, lvl, phaser):

    if lvl == 0:
        t.forward(length)
    else:
        t.left(phaser * 45)
        dragon(t, length / m.sqrt(2), lvl - 1, -1)
        t.right(phaser * 90)
        dragon(t, length / m.sqrt(2), lvl - 1, 1)
        t.left(phaser * 45)


# %% testing code (only runs if this is main script)
if __name__ == '__main__':

    window = turtle.Screen()

    dragon(t=setup(), length=400, lvl=9, phaser=1)

