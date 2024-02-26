#!/usr/bin/python3
import random
number = random.randint(-10, 10)

print(f'{number} ', end='')

print('is positive') if number > 0 else (
    print('is zero') if number == 0 else print('is negative')
    )
