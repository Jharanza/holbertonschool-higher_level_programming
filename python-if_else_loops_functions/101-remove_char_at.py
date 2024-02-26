#!/usr/bin/python3
''' remove the character in the n position of the string 
    Return: the new string, or the old if n is negative
'''

def remove_char_at(str, n):
    new_arr = str[0:]

    if len(str) < n or n < 0:
        return new_arr

    other = new_arr.replace(new_arr[n], '')
    return ''.join(other)
