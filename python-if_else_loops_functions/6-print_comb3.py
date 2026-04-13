#!/usr/bin/python3
''' Prints the differents conbinations of two digits '''

for x in range(9):
  for y in range(10):
    if x < y:
      if x != 8 or y != 9:
        print(f'{x}{y}, ', end='')
      else:
        print(f'{x}{y}') 
