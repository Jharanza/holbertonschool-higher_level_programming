#!/usr/bin/python3
import hidden_4

for elem in dir(hidden_4):
  if not elem.startswith('__'):
    print(elem)
