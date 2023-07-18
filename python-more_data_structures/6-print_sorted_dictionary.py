#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = sorted(a_dictionary.keys())
    for element in new_dict:
        value = a_dictionary[element]
        print("{}: {}".format(element, value))
