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
    for i in range(len(v.argv)):
        if i > 0:
            print(f"{i}: {v.argv[i]}")
