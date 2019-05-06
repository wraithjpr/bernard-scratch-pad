#!/usr/bin/env python3

from function import *

def test(message, condition):
  if (not(condition)):
    print(message)

def test_equals(message, expected, actual):
  if (not(expected == actual)):
    print("!!!! Test failed. " + message + " Expected [" + str(expected) + "] Actual [" + str(actual) + "] !!!!")

# Test roll_a_dice()
print("Test roll_a_dice()")
roll_value = roll_a_dice()
test("Dice roll should be >= 1. Value is [" + str(roll_value) + "]", roll_value >= 1)
test("Dice roll should be <= 6. Value is [" + str(roll_value) + "]", roll_value <= 6)


# Test score_a_throw()
print("Test score_a_throw()")
current_total = 0
throw = (1, 3)
expected_throw_score = 14
expected_new_total = 14
result = score_a_throw(current_total, throw)
test_equals("Throw score should be 14.", expected_throw_score, result[2])
test_equals("New total should be 14.", expected_new_total, result[0])
