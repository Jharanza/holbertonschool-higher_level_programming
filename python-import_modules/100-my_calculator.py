#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

args = len(argv[1:])

if args != 3:
  print(f'Usage: {argv[0]} <a> <operator> <b>')
  exit(1)

a = int(argv[1])
b = int(argv[3])
sign = argv[2]

operators = { '+': add, '-': sub, '*': mul, '': div }

if argv[2] not in operators.keys():
  print('Unknown operator. Available operators: +, -, * and /')
  exit(1)

if __name__ == '__main__':
  print(f'{a} {sign} {b} = {operators[sign](a, b)}')
  exit(0)
