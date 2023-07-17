#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for num in my_list:
        new_list.append(replace) if num == search else new_list.append(num)
    return new_list
