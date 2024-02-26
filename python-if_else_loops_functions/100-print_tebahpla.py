#!/usr/bin/python3
''' print the ASCII alphabet in reversed order between lower and uppercase '''

for x in range(122, 96, -1):
    if x % 2 != 0:
        x = x - 32
    print(chr(x), end='')
