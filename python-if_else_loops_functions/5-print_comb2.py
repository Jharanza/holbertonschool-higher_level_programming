#!/usr/bin/python3
''' Print the numbers from 0 to 99 '''

for x in range(100):
    if x < 10:
        x = '0' + str(x)
    print(f'{x}, ', end='') if x != 99 else print(x)
