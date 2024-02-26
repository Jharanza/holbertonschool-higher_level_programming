#!/usr/bin/python3
''' Prints the differents conbinations of two digits '''

for x in range(9):
    for y in range(10):
        if x < y:
            print(f'{x}{y}, ', end='') if x != 8 or y != 9 else print(f'{x}{y}')
