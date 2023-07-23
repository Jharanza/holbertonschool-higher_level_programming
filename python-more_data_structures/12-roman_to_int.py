#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    if roman_string is None:
        return 0
    numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }

    total = 0
    prev_val = 0

    for symbol in reversed(roman_string):
        value = numerals.get(symbol, 0)
        if value >= prev_val:
            total += value
        else:
            total -= value
        prev_val = value

    return total
