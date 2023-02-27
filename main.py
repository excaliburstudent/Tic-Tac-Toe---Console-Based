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
CAT = "cat"

WHO_SHOULD_GO_FIRST_PROMPT = "Who should go first? "
INVALID_PLAYER_CHOICE_ERROR = "Please enter a number between 1 and 9."

WINNING_COMBINATIONS = [
  [ 1, 2, 3 ],
  [ 1, 5, 9 ],
  [ 1, 4, 7 ],
  [ 2, 5, 8 ],
  [ 3, 6, 9 ],
  [ 3, 5, 7 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]

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

def can_win(the_board, symbol):
  for combination in WINNING_COMBINATIONS:
    first_symbol = the_board[combination[0] - 1]
    second_symbol = the_board[combination[1] - 1]
    third_symbol = the_board[combination[2] - 1]

    if first_symbol == symbol and second_symbol == symbol and third_symbol == EMPTY:
      return combination[2]
    elif first_symbol == symbol and third_symbol == symbol and second_symbol == EMPTY:
      return combination[1]
    elif second_symbol == symbol and third_symbol == symbol and first_symbol == EMPTY:
      return combination[0]

  return None

def prevent_two_option_win(the_board, p1, p2, e1, e2, e3):
  first_symbol = the_board[p1 - 1]
  second_symbol = the_board[p2 - 1]
  third_symbol = the_board[5 - 1]
  if first_symbol == PLAYER and second_symbol == PLAYER and third_symbol == COMPUTER:
    first_symbol = the_board[e1 - 1]
    second_symbol = the_board[e2 - 1]
    third_symbol = the_board[e3 - 1]
    if first_symbol == EMPTY and second_symbol == EMPTY and third_symbol == EMPTY:
      return e3

  return None

def center_or_corner_square(the_board):
  squares = [ 5, 1, 3, 7, 9 ]
  for square in squares:
    if the_board[square - 1] == EMPTY:
      return square

  return None
  
def get_computer_choice(the_board):
  print("It's my turn.")
  time.sleep(random.randint(25, 75)/100)
  choice = can_win(the_board, COMPUTER)
  if choice == None:
    choice = can_win(the_board, PLAYER)
  if choice == None:
    choice = prevent_two_option_win(the_board, 1, 9, 4, 7, 8)
  if choice == None:
    choice = prevent_two_option_win(the_board, 1, 8, 9, 4, 7)
  if choice == None:
    choice = prevent_two_option_win(the_board, 3, 7, 8, 9, 6)
  if choice == None:
    choice = prevent_two_option_win(the_board, 3, 8, 9, 7, 6)
  if choice == None:
    choice = prevent_two_option_win(the_board, 7, 6, 9, 8, 3)
  if choice == None:
    choice = center_or_corner_square(the_board)
  if choice == None:
    choice = random.randint(1, 9)
    while the_board[choice - 1] != EMPTY:
      time.sleep(random.randint(25, 50)/100)
      choice = random.randint(1, 9)
      
  return choice

def check_for_winner(the_board):
  for combination in WINNING_COMBINATIONS:
    first_symbol = the_board[combination[0] - 1]
    second_symbol = the_board[combination[1] - 1]
    third_symbol = the_board[combination[2] - 1]
    if first_symbol != EMPTY and second_symbol == first_symbol and third_symbol == first_symbol:
      return first_symbol

  if the_board.count(EMPTY) == 0:
    return CAT

  return None

def report_winner(the_winner):
  if the_winner == PLAYER:
    print("Congratulations!  You won the game!")
  elif the_winner == COMPUTER:
    print("Ha!  I won!")
  else:
    print("Ah, we tied.  Cat got that game.")

def play_game():
  random.seed()
  whose_turn = greet_player()
  draw_board(board)
  
  winner = None
  while winner == None:
    if whose_turn == PLAYER:
      player_choice = get_player_choice(board)
      board[player_choice - 1] = PLAYER
      whose_turn = COMPUTER
    else:
      computer_choice = get_computer_choice(board)
      board[computer_choice - 1] = COMPUTER
      whose_turn = PLAYER
  
    draw_board(board)
    winner = check_for_winner(board)
  
  report_winner(winner)

play_game()
