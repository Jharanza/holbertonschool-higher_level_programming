#!/usr/bin/python3
if __name__ == "__main__":
    import sys as v
    arg = len(v.argv) - 1
    if arg == 1:
        print(f"{arg} argument:") 
    elif arg == 0:
        print(f"{arg} arguments.")
    else:
        print(f"{arg} arguments:")
    for i in range(arg + 1):
        if i > 0:
            print(f"{i}: {v.argv[i]}")
