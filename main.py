# Tic Tac Toe - Console-Based
#
# This program will allow the user to play Tic Tac Toe against
# the computer.  The board will be drawn in text-characters on
# the screen.
#
# Author: Robert Walsh
# Date Created: January 29, 2023

EMPTY = "empty"
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

print("Hello, let's play Tic Tac Toe.")
print("I'll be X and you can be O.")

whose_turn = input("Who should go first? ").upper()
while whose_turn != "X" and whose_turn != "O":
  print("Please enter X or O.")
  whose_turn = input("Who should go first? ").upper()
  
draw_board(board)
