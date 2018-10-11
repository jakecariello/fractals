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
    if n == 0:
        return axiom
    else:
        return ''.join([expand(rules.get(char, ''), rules, n - 1) for char in axiom])


def draw(string, alphabet, types, n, stack=[]):

    """
    NOTE: Uses recursion!!!

    :param n: the current layer of recursion
    :param string: STRING containing characters in the alphabet. Each character corresponds to a command.
    :param alphabet: DICT with the character as the key, then a tuple of the command type,
                        the actual function to be called, and a scale factor (relating to previous iteration)
                        NOTE: the scale should default to 1 if not specified?
    :param types: DICT with a command type (str) as key, and the associated reference magnitude (float) as value
    :param stack: LIST containing tuples of (x, y, length, angle). Opening bracket signals entry
                    into new push, and a closed bracket pops the last tuple so drawing may resume from before pushed.
                    NOTE: expects that the command of a push type will return its position and direction in
                    a 3-term tuple. The command of a pop type should both set the position and angle from the push data.
    :return: the current string and stack
    """

    for char in string:
        string = string[1 : len(string)]
        (kind, command, scale) = alphabet[char]

        if kind is 'push':
            stack.append(command(types[kind]))  # should return (x, y, angle)
            #print(stack)
            n += 1

        elif kind is 'pop':
            command(types[kind], stack.pop())  # should go to x, y and turn to angle
            #print(stack)
            n -= 1

        elif kind is 'none':
            pass

        else:
            command(types[kind] * scale)


def get_state(t: turtle.Turtle):
    return t.xcor(), t.ycor(), t.heading()


def set_state(t: turtle.Turtle, state: tuple):
    print('GO TO {}'.format(state))
    t.penup()
    t.setposition(state[0], state[1])
    t.setheading(state[2])
    t.pendown()

if __name__ == '__main__':

    window = turtle.Screen()
    franklin = turtle.Turtle()
    franklin.speed(0)

    rules = {'X': 'F+[[X]-X]-F[-FX]+X',
             'F': 'FF'}
    axiom = 'X'

    expanded = expand(axiom, rules, 3)

    types = {'move': 10,
             'turn': 25,
             'push': franklin,
             'pop': franklin}

    alphabet = {'X': ('none', None, None),
                'F': ('move', franklin.forward, 1),
                '-': ('turn', franklin.left, 1),
                '+': ('turn', franklin.left, -1),
                '[': ('push', get_state, franklin),
                ']': ('pop', set_state, franklin)}

    draw(expanded, alphabet, types, 3)
