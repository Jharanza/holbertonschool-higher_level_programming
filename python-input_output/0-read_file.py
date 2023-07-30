#!/usr/bin/python3
''' module 0-read_file that prints the content of a file '''


def read_file(filename=""):
    '''
        method that read files and prints it
        Args:
            filename: The document to print
    '''
    with open(filename, encoding="utf-8") as my_file:
        content = my_file.read()
    print(content, end="")
