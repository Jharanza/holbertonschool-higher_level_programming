#!/usr/bin/python3
''' return the last digit of a number '''

def print_last_digit(number):
    last = abs(number) % 10
    print(last, end='')

    return last
