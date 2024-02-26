#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last = number % 10 if number >= 0 else ((number * -1) % 10) * -1

print(f'Last digit of {number} is {last} ', end='')

print('and is greater than 5') if last > 5 else (
    print('and is 0') if last == 0 else print('and is less than 6 and not 0')
    )
