# Tic Tac Toe - Console-Based
#
# This program will allow the user to play Tic Tac Toe against
# the computer.  The board will be drawn in text-characters on
# the screen.
#
# Author: Robert Walsh
# Date Created: January 29, 2023

EMPTY = "empty"
COMPUTER = "X"
PLAYER = "O"

WHO_SHOULD_GO_FIRST_PROMPT = "Who should go first? "

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

whose_turn = greet_player()
draw_board(board)

print("It's player {}'s turn".format(whose_turn))