#!/usr/bin/python3
''' return the last digit of a number '''

def print_last_digit(number):
    last = number % 10 if number >= 0 else (number * -1) % 10
    print(last, end='')
    return last
