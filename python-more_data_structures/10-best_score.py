#!/usr/bin/python3

def best_score(a_dictionary):
  if a_dictionary is None or len(a_dictionary) == 0:
    return None

  best = 0
  studen = ''

  for k, v in a_dictionary.items():
    if v > best:
      best = v
      studen = k

  return studen
