#!/usr/bin/env python3

#%load_ext pycodestyle_magic # if using google colab

import sys
from solution import solution

print("Submit a number and get an answer!\n")
while True:
    try:
        n = input("Number: ").lower()
        if (n == "exit"):
            print("You entered exit, bye!")
            break
        solution(n)
    except KeyboardInterrupt:
        print("KeyboardInterrupt. Stopping...\n")
        break