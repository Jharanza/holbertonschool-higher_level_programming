#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    m = ""
    for i in range(x):
        try:
            m += str(my_list[i])
            n += 1
        except Exception:
            pass
    print("{:s}".format(m))
    return n
