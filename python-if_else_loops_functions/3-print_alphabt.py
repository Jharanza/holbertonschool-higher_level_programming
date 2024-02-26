#!/usr/bin/python3
''' Print the alphabet in ASCII lowercase without q and e '''

for x in range(97, 123):
    if chr(x) != 'q' and chr(x) != 'e':
        print(chr(x), end='')
