#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cont = 0
    try:
        for y in range(x):
            if type(my_list[y]) == int:
                print("{:d}".format(my_list[y]), end="")
                cont += 1
    except (ValueError, TypeError):
        pass
    print()
    return cont
