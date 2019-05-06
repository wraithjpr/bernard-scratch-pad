from random import randint
from random import seed

DICE_SIZE = 6
AUTHORISED_USERS = {
  "Bernard",
  "Eduad"
  "Edwin",
  "James"
}

# Set up dice
# This seeds the random number generator.
# Call this once at the start of the game
def set_up_dice():
  seed()

# Roll a dice
def roll_a_dice():
  return  randint(1, DICE_SIZE)

# Does a throw, by rolling the dice twice, and returns the result in a tuple
def do_a_dice_throw():

  first_roll_value = roll_a_dice()
  second_roll_value = roll_a_dice()

  throw = (first_roll_value, second_roll_value)
  return throw

# Given a number, returns true if even, false if odd
# So, take modulus 2 of the number to get the remainder. All even numbers will give a remainder of zero. 
def is_even(num):
  remainder = num % 2
  if (remainder == 0):
    return True
  else:
    return False

# Given a running total and a throw, work out the points scored this throw and the new running total
def score_a_throw(current_total, throw):
  # Initialise the new total to the current toal
  new_total = current_total

  # The points rolled on the dice are added to the score
  points_rolled = throw[0] + throw[1]
  new_total = new_total + points_rolled

  # if(is_even(new_total)):
  if(is_even(points_rolled)):
    new_total = new_total + 10      # If the total is an even number, you get an additional 10 points
  else:
    new_total = new_total - 5       # If the total is an odd number, you get 5 points taken off
    new_total = max(new_total, 0)   # The score cannot go below zero at any point

  # Check for a double
  if(throw[0] == throw[1]):
    new_total = new_total + roll_a_dice()

  return (new_total, throw, new_total - current_total)

# Returns True when a given name is an authosised user, False otherwise.
def is_authorised_user(name):
  return name in AUTHORISED_USERS