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

class Game:
  
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

  def __init__(self):
    self.board = [ 
      Game.EMPTY, Game.EMPTY, Game.EMPTY, 
      Game.EMPTY, Game.EMPTY, Game.EMPTY, 
      Game.EMPTY, Game.EMPTY, Game.EMPTY 
    ]
    
  def get_symbol(self, square_number):
    symbol = self.board[square_number - 1]
    if symbol == Game.EMPTY:
      return square_number
  
    return symbol
    
  def draw_board(self):
    for row in range(3):
      print("   |   |   ")
      print(" {} | {} | {} ".format(self.get_symbol(row * 3 + 1), self.get_symbol(row * 3 + 2), self.get_symbol(row * 3 + 3)))
      print("   |   |   ")
      if row < 2:
        print("---+---+---")
    
  def greet_player(self):
    print("Hello, let's play Tic Tac Toe.")
    print("I'll be {} and you can be {}.".format(Game.COMPUTER, Game.PLAYER))
  
    choice = input(Game.WHO_SHOULD_GO_FIRST_PROMPT).upper()
    while choice != Game.COMPUTER and choice != Game.PLAYER:
      print("Please enter {} or {}.".format(Game.COMPUTER, Game.PLAYER))
      choice = input(Game.WHO_SHOULD_GO_FIRST_PROMPT).upper()
    return choice
  
  def get_player_choice(self):
    print("It's your turn.")
    valid_choice = False
    while not valid_choice:
      choice = input("Pick a square by typing its number: ")
      if not choice.isdecimal():
        print(Game.INVALID_PLAYER_CHOICE_ERROR)
      else:
        choice = int(choice)
        if choice < 1 or choice > 9:
          print(Game.INVALID_PLAYER_CHOICE_ERROR)
        elif self.board[choice - 1] != Game.EMPTY:
          print("That square is already taken.")
        else:
          valid_choice = True
    return choice
  
  def can_win(self, symbol):
    for combination in Game.WINNING_COMBINATIONS:
      first_symbol = self.board[combination[0] - 1]
      second_symbol = self.board[combination[1] - 1]
      third_symbol = self.board[combination[2] - 1]
  
      if first_symbol == symbol and second_symbol == symbol and third_symbol == Game.EMPTY:
        return combination[2]
      elif first_symbol == symbol and third_symbol == symbol and second_symbol == Game.EMPTY:
        return combination[1]
      elif second_symbol == symbol and third_symbol == symbol and first_symbol == Game.EMPTY:
        return combination[0]
  
    return None
  
  def prevent_two_option_win(self, p1, p2, e1, e2, e3):
    first_symbol = self.board[p1 - 1]
    second_symbol = self.board[p2 - 1]
    third_symbol = self.board[5 - 1]
    if first_symbol == Game.PLAYER and second_symbol == Game.PLAYER and third_symbol == Game.COMPUTER:
      first_symbol = self.board[e1 - 1]
      second_symbol = self.board[e2 - 1]
      third_symbol = self.board[e3 - 1]
      if first_symbol == Game.EMPTY and second_symbol == Game.EMPTY and third_symbol == Game.EMPTY:
        return e3
  
    return None
  
  def center_or_corner_square(self):
    squares = [ 5, 1, 3, 7, 9 ]
    for square in squares:
      if self.board[square - 1] == Game.EMPTY:
        return square
  
    return None
    
  def get_computer_choice(self):
    print("It's my turn.")
    time.sleep(random.randint(25, 75)/100)
    choice = self.can_win(Game.COMPUTER)
    if choice == None:
      choice = self.can_win(Game.PLAYER)
    if choice == None:
      choice = self.prevent_two_option_win(1, 9, 4, 7, 8)
    if choice == None:
      choice = self.prevent_two_option_win(1, 8, 9, 4, 7)
    if choice == None:
      choice = self.prevent_two_option_win(3, 7, 8, 9, 6)
    if choice == None:
      choice = self.prevent_two_option_win(3, 8, 9, 7, 6)
    if choice == None:
      choice = self.prevent_two_option_win(7, 6, 9, 8, 3)
    if choice == None:
      choice = self.center_or_corner_square()
    if choice == None:
      choice = random.randint(1, 9)
      while self.board[choice - 1] != Game.EMPTY:
        time.sleep(random.randint(25, 50)/100)
        choice = random.randint(1, 9)
        
    return choice

  def check_for_winner(self):
    for combination in Game.WINNING_COMBINATIONS:
      first_symbol = self.board[combination[0] - 1]
      second_symbol = self.board[combination[1] - 1]
      third_symbol = self.board[combination[2] - 1]
      if first_symbol != Game.EMPTY and second_symbol == first_symbol and third_symbol == first_symbol:
        return first_symbol
  
    if self.board.count(Game.EMPTY) == 0:
      return Game.CAT
  
    return None
  
  def report_winner(self, the_winner):
    if the_winner == Game.PLAYER:
      print("Congratulations!  You won the game!")
    elif the_winner == Game.COMPUTER:
      print("Ha!  I won!")
    else:
      print("Ah, we tied.  Cat got that game.")
  
  def play_game(self):
    random.seed()
    whose_turn = self.greet_player()
    self.draw_board()

    winner = None
    while winner == None:
      if whose_turn == Game.PLAYER:
        player_choice = self.get_player_choice()
        self.board[player_choice - 1] = Game.PLAYER
        whose_turn = Game.COMPUTER
      else:
        computer_choice = self.get_computer_choice()
        self.board[computer_choice - 1] = Game.COMPUTER
        whose_turn = Game.PLAYER
    
      self.draw_board()
      winner = self.check_for_winner()
    
    self.report_winner(winner)

game = Game()
game.play_game()
