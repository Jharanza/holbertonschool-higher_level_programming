#!/usr/bin/python3
'''
    module 0-add_integer return the suma of 2 int
'''


def add_integer(a, b=98):
    '''
        add_integer method returns a integer
        args:
            a: first agument
            b: second argument
            c: the result of a + b
            return: the suma of a and b
    '''

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    c = a + b

    return c
