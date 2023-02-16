# Tic Tac Toe - Console-Based
#
# This program will allow the user to play Tic Tac Toe against
# the computer.  The board will be drawn in text-characters on
# the screen.
#
# Author: Robert Walsh
# Date Created: January 29, 2023

import random
import time

EMPTY = "empty"
COMPUTER = "X"
PLAYER = "O"

WHO_SHOULD_GO_FIRST_PROMPT = "Who should go first? "
INVALID_PLAYER_CHOICE_ERROR = "Please enter a number between 1 and 9."

board = [ 
  EMPTY, EMPTY, EMPTY, 
  EMPTY, EMPTY, EMPTY, 
  EMPTY, EMPTY, EMPTY 
]

def get_symbol(the_board, square_number):
  symbol = the_board[square_number - 1]
  if symbol == EMPTY:
    return square_number

  return symbol
  
def draw_board(the_board):
  for row in range(3):
    print("   |   |   ")
    print(" {} | {} | {} ".format(get_symbol(the_board, row * 3 + 1), get_symbol(the_board, row * 3 + 2), get_symbol(the_board, row * 3 + 3)))
    print("   |   |   ")
    if row < 2:
      print("---+---+---")

def greet_player():
  print("Hello, let's play Tic Tac Toe.")
  print("I'll be {} and you can be {}.".format(COMPUTER, PLAYER))

  choice = input(WHO_SHOULD_GO_FIRST_PROMPT).upper()
  while choice != COMPUTER and choice != PLAYER:
    print("Please enter {} or {}.".format(COMPUTER, PLAYER))
    choice = input(WHO_SHOULD_GO_FIRST_PROMPT).upper()
  return choice

def get_player_choice(the_board):
  print("It's your turn.")
  valid_choice = False
  while not valid_choice:
    choice = input("Pick a square by typing its number: ")
    if not choice.isdecimal():
      print(INVALID_PLAYER_CHOICE_ERROR)
    else:
      choice = int(choice)
      if choice < 1 or choice > 9:
        print(INVALID_PLAYER_CHOICE_ERROR)
      elif the_board[choice - 1] != EMPTY:
        print("That square is already taken.")
      else:
        valid_choice = True
  return choice

def get_computer_choice(the_board):
  print("It's my turn.")
  time.sleep(random.randint(25, 75)/100.0)
  choice = random.randint(1, 9)
  while the_board[choice - 1] != EMPTY:
    time.sleep(random.randint(25, 50)/100.0)
    choice = random.randint(1, 9)

  return choice

random.seed()
whose_turn = greet_player()
draw_board(board)

#player_choice = get_player_choice(board)
#print("You chose: {}".format(player_choice))

computer_choice = get_computer_choice(board)
print("I chose {}".format(computer_choice))