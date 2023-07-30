#!/usr/bin/python3
'''
    Module 1-write_file that writes a file and return the numbers
    of characters written
'''


def write_file(filename="", text=""):
    '''
        Method that over-write a file and returns the numbers of
        characters written
        Args:
            filename: document to over-write
            text: text to write in the file
        return: the numbers written in the file
    '''
    with open(filename, "w", encoding='utf-8') as my_file:
        my_file.write(text)
    return len(text)
