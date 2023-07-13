#!/usr/bin/python3
def uppercase(str):
    for i in str:
        ch = ord(i)
        if 96 <= ch <= 122:
            ch -= 32
        print(chr(ch), end='')
    print()
