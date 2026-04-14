#!/usr/bin/python3
from sys import argv

args = len(argv[1:])

if __name__ == '__main__':
  print(f'{args} {"argument" if args == 1 else "arguments"}{'.' if args == 0 else ':'}')
  for i in range(args):
    if args > 0:
      print(f'{i + 1}: {argv[i + 1]}')
