"""
File: lindemayer.py
Date: 10/9/2018
Author: Jake Cariello
Purpose: Draw an L-system using an axiom string and angle (∂).
         For info: see: https://en.wikipedia.org/wiki/L-system
"""

# %% Imports
import turtle

# %% Define functions
def test(alpha):
    alpha['A'](100)




if __name__ == '__main__':

    window = turtle.Screen()
    franklin = turtle.Turtle()

    # form: KEY : (function, param scale)
    # relies on a standard length/angle ---> altered  by param scale
    alphabet = {'A': franklin.forward}

    test(alphabet)
