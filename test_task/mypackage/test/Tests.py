#!/usr/bin/env python3

import unittest
from solution import solution

class TestClass(unittest.TestCase):
  def test_FizzBuzz():
    digit = 15
    assert solution(digit) == "FizzBuzz!"
  def test_Fizz():
    digit = 9
    assert solution(digit) == "Fizz!"
  def test_Buzz():
    digit = 5
    assert solution(digit) == "Buzz!"
  def test_NO_FizzBuzz():
    digit = 1
    assert solution(digit) == "This number is not aliquot on 3 or 5"
  def test_NoSolve():
    digit = "12412ewq"
    assert solution(digit) == "Well, i got no idea what u've entered, but i couldn't solve your number.\nLets start again"
  def test_Exit():
    digit = "Exit"
    assert solution(digit) == "You entered exit, bye!"
  def pytest_keyboard_interrupt(excinfo):
    digit = "KeyboardInterrupt"
    
if __name__ == "__main__":
  unittest.main()