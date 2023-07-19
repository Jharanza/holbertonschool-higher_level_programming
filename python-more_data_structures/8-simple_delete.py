#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    '''Deleting a ke in a dictionary
    :param key: argument type string
    :param a_dicitionary: dictionary to be change
    :return: a dictionary
    '''
    if a_dictionary.get(key):
        a_dictionary.pop(key)
    return a_dictionary
