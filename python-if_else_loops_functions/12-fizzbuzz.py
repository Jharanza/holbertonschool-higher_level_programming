#!/usr/bin/python3
''' Print the number from 1 to 100 '''

def fizzbuzz():
    for x in range(1, 101):
        print('FizzBuzz ', end='') if x % 15 == 0 else (
            print('Buzz ', end='') if x % 5 == 0 else (
                print('Fizz ', end='') if x % 3 == 0 else print(
                    f'{x} ', end='')))
