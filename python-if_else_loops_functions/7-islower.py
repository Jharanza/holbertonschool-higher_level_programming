#!/usr/bin/python3
''' Check for lowercase characters '''

def islower(c: str) -> bool:
    if ord(c) in range(97, 123):
        return True
    return False
