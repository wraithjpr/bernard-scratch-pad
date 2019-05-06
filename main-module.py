#!/usr/bin/env python3

from hello import say_hello

from function import *

say_hello("world")
say_hello("Bernard")

# Seed the random number dice
set_up_dice()

# Let's try out some dice rolls
dice_roll_value = roll_a_dice()

print("Dice roll value is: " + str(dice_roll_value))


first_roll_value = roll_a_dice()
print("First roll value is: " + str(first_roll_value))
second_roll_value = roll_a_dice()
print("Second roll value is: " + str(second_roll_value))

# Let's call rolling two six-sided dice, a throw.
# So, Player 1 will have a throw, then player 2 will have a throw.

''' Our first try...
first_roll_value_player1 = roll_a_dice()
print("First roll value for player 1 is: " + str(first_roll_value_player1))
second_roll_value_player1 = roll_a_dice()
print("Second roll value for player 1 is: " + str(second_roll_value_player1))

throw_player1 = (first_roll_value_player1, second_roll_value_player1)
print("Player 1's throw is: " + str(throw_player1))

first_roll_value_player2 = roll_a_dice()
print("First roll value for player 2 is: " + str(first_roll_value_player2))
second_roll_value_player2 = roll_a_dice()
print("Second roll value for player 2 is: " + str(second_roll_value_player2))

throw_player2 = (first_roll_value_player2, second_roll_value_player2)
print("Player 2's throw is: " + str(throw_player2))
'''

# dice throws
throw_player1 = do_a_dice_throw()
print("Player 1's throw is: " + str(throw_player1))

throw_player2 = do_a_dice_throw()
print("Player 2's throw is: " + str(throw_player2))

# Let's call the two players' throws a 'round'
round = (throw_player1, throw_player2)
print("The round result is: " + str(round))

# We do five rounds in a game
INITIAL_TOTAL = 0

# Round tuple indexes
PLAYER_ONE = 0
PLAYER_TWO = 1

# Score a throw result tuple indexes
NEW_TOTAL = 0
THROW = 1
THROW_SCORE = 2

# Throw tuple indexes
ROLL1 = 0
ROLL2 = 1


# Construct the five round tuples
round1 = (
  score_a_throw(INITIAL_TOTAL, do_a_dice_throw()),    # Player 1
  score_a_throw(INITIAL_TOTAL, do_a_dice_throw())     # Player 2
)

player1_accumulated_score_after_round1 = round1[PLAYER_ONE][NEW_TOTAL]
player2_accumulated_score_after_round1 = round1[PLAYER_TWO][NEW_TOTAL]

round2 = (
  score_a_throw(player1_accumulated_score_after_round1, do_a_dice_throw()),
  score_a_throw(player2_accumulated_score_after_round1, do_a_dice_throw())
)

player1_accumulated_score_after_round2 = round2[PLAYER_ONE][NEW_TOTAL]
player2_accumulated_score_after_round2 = round2[PLAYER_TWO][NEW_TOTAL]

round3 = (
  score_a_throw(player1_accumulated_score_after_round2, do_a_dice_throw()),
  score_a_throw(player2_accumulated_score_after_round2, do_a_dice_throw())
)

player1_accumulated_score_after_round3 = round3[PLAYER_ONE][NEW_TOTAL]
player2_accumulated_score_after_round3 = round3[PLAYER_TWO][NEW_TOTAL]

round4 = (
  score_a_throw(player1_accumulated_score_after_round3, do_a_dice_throw()),
  score_a_throw(player2_accumulated_score_after_round3, do_a_dice_throw())
)

player1_accumulated_score_after_round4 = round4[PLAYER_ONE][NEW_TOTAL]
player2_accumulated_score_after_round4 = round4[PLAYER_TWO][NEW_TOTAL]

round5 = (
  score_a_throw(player1_accumulated_score_after_round4, do_a_dice_throw()),
  score_a_throw(player2_accumulated_score_after_round4, do_a_dice_throw())
)

player1_accumulated_score_after_round5 = round5[PLAYER_ONE][NEW_TOTAL]
player2_accumulated_score_after_round5 = round5[PLAYER_TWO][NEW_TOTAL]


# Construct the game tuple from the five round tuples
game = (round1, round2, round3, round4, round5)
print("The game's rounds are: " + str(game))

if (player1_accumulated_score_after_round5 > player2_accumulated_score_after_round5):
  print("The winner is Player 1: winning " + str(player1_accumulated_score_after_round5) + " points to " + str(player2_accumulated_score_after_round5) + ".")
elif (player1_accumulated_score_after_round5 < player2_accumulated_score_after_round5):
  print("The winner is Player 2: winning " + str(player2_accumulated_score_after_round5) + " points to " + str(player1_accumulated_score_after_round5) + ".")
else:
  print("It's a draw: " + str(player1_accumulated_score_after_round5) + " points each.")




# Is a number even?
even_number = 4
even_number_divided_by_2 = even_number / 2

print("Even number divided by 2 is: " + str(even_number_divided_by_2))

print(str(4 % 2))
print(str(5 % 2))


# Techniques for authorised users.
print("Is Bernard authorised?..." + str(is_authorised_user("Bernard")))
print("Is DobbyDo authorised?..." + str(is_authorised_user("DobbyDo")))


player1 = input("Who is player 1? Enter your name: ")
if(is_authorised_user(player1)):
  print("You may play... best of luck!")
else:
  print("Don't know you... go away.")
