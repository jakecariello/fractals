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

def expand(axiom, rules, n):
    if n == 0:
        return axiom
    else:
        return ''.join([expand(rules[char], rules, n - 1) for char in axiom])


def draw(string, alphabet, length, angle, stack=[]):
    for (step, scale) in [alphabet[char] for char in string]:
        #step()
        pass
# TODO: add trait to distinguish btwn a move and a pivot!
# TODO: ADD DOCUMENTATION, or it'll all be forgotten/unreadable

if __name__ == '__main__':

    window = turtle.Screen()
    franklin = turtle.Turtle()

    # form: KEY : (function, param scale)
    # relies on a standard length/angle ---> altered  by param scale
    alphabet = {'A': franklin.forward}
    rules = {'A': 'AB',
             'B': 'A'}

    #test(alphabet)

    expanded = expand('A', rules, 5)

    draw('',alphabet,10,10)