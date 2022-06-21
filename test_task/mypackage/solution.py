#!/usr/bin/env python3

def solution(n):
    try:
        n = int(n)
        if (n % 3 == 0 and n % 5 == 0):
            print("FizzBuzz!\n")
        elif (n % 3 == 0):
            print("Fizz!\n")
        elif (n % 5 == 0):
            print("Buzz!\n")
        else:
            print("This number is not aliquot on 3 or 5\n")
    except (RuntimeError, TypeError, NameError, ValueError):
        print("Well, i got no idea what u've entered, but i couldn't solve your number.\nLets start again")