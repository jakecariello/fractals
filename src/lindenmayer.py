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
def expand(axiom, rules, n):
    """
    :param axiom: STRING used as base that will be expanded
    :param rules: DICT of characters with their associated expansions
    :param n: INT current level of recursion (where highest number is the "outside")
    :return:
    """

    if n == 0:
        return axiom
    else:
        return expand(''.join([rules.get(char, char) for char in axiom]), rules, n - 1)


def draw(string, alphabet, types, n, stack=[]):
    """
    :param string: STRING containing characters in the alphabet. Each character corresponds to a command.
    :param alphabet: DICT with the character as the key, then a tuple of the command type,
                        the actual function to be called, and a scale factor (relating to previous iteration)
                        NOTE: the scale should default to 1 if not specified?
    :param types: DICT with a command type (str) as key, and the associated reference magnitude (float) as value
    :param n: the current layer of recursion
    :param stack: LIST containing tuples of (x, y, length, angle). Opening bracket signals entry
                    into new push, and a closed bracket pops the last tuple so drawing may resume from before pushed.
                    NOTE: expects that the command of a push type will return its position and direction in
                    a 3-term tuple. The command of a pop type should both set the position and angle from the push data.
    """

    for char in string:
        string = string[1: len(string)]
        (kind, command, scale) = alphabet[char]

        if kind is 'push':
            stack.append(command(types[kind]))  # should return (x, y, angle)
            n += 1

        elif kind is 'pop':
            command(types[kind], stack.pop())  # should go to x, y and turn to angle
            n -= 1

        elif kind is 'control':  # this character is used for rule expansion and should be ignored
            pass

        else:
            command(types[kind] * scale)


def get_state(t: turtle.Turtle):
    return t.xcor(), t.ycor(), t.heading()


def set_state(t: turtle.Turtle, state: tuple):
    t.penup()
    t.setposition(state[0], state[1])
    t.setheading(state[2])
    t.pendown()


def setup():
    t = turtle.Turtle()
    t.penup()
    t.setposition(-300, -300)
    t.setheading(60)
    t.pendown()
    t.speed(0)
    return t


if __name__ == '__main__':
    franklin = setup()

    axiom = 'X'
    rules = {'X': 'F+[[X]-X]-F[-FX]+X',
             'F': 'FF'}
    types = {'move': 5,
             'turn': 25,
             'push': franklin,
             'pop': franklin}
    alphabet = {'X': ('control', None, None),
                'F': ('move', franklin.forward, 1),
                '+': ('turn', franklin.left, 1),
                '-': ('turn', franklin.left, -1),
                '[': ('push', get_state, franklin),
                ']': ('pop', set_state, franklin)}

    expanded = expand(axiom, rules, 6)
    draw(expanded, alphabet, types, 3)

    franklin.hideturtle()  # hide the turtle after drawing
