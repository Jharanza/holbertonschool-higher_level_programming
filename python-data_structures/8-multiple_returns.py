#!/usr/bin/python3
''' Returns a tuple with the length of a string and its first character '''

def multiple_returns(sentence):
    str_l = len(sentence)
    first = None
    my_list = [str_l, first]


    if str_l == 0:
        first = None
    else:
        first = sentence[0]
        my_list[1] = first

    return tuple(my_list)
