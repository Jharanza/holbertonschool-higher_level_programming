#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    u_digit = ((number * -1) % 10) * -1
else:
    u_digit = number % 10

if u_digit == 0:
    print(f"Last digit of {number} is {u_digit} and is 0")
elif u_digit > 5:
    print(f"Last digit of {number} is {u_digit} and is greater than 5")
elif u_digit < 6:
    print(f"Last digit of {number} is {u_digit} and is less than 6 and not 0")
