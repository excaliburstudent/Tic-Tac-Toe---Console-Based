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

def draw_board():
  print("   |   |   ")
  print(" 1 | 2 | 3 ")
  print("   |   |   ")
  print("---+---+---")
  print("   |   |   ")
  print(" 4 | 5 | 6 ")
  print("   |   |   ")
  print("---+---+---")
  print("   |   |   ")
  print(" 7 | 8 | 9 ")
  print("   |   |   ")

draw_board()
