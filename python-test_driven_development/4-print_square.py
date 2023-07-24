#!/usr/bin/python3
'''
    4-print_square module prints a square
'''


def print_square(size):
    '''
        print_square method prints a square
        Args:
            size: The size of the square
            return: nothing
    '''

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    size = int(size)

    for i in range(size):
        fig = ""
        for j in range(size):
            fig += "#"
        print(fig)
