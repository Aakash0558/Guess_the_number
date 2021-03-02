import random
from art import logo

def game_mode(number, mode):
  if mode == "easy":
    attempts = 10
  else:
    attempts = 5
  while attempts != 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > 100 or guess < 1:
      #for out of bounds guesses
      print("Your guess is out of bounds, you lose one attempt.")
      attempts -= 1
      if attempts == 0:
        print("You've run out of guesses, you lose.")
        print(f"The correct number was {number}.")
      else:
        print("Guess again.")
    elif guess > number:
      print("Too high.")
      attempts -= 1
      if attempts == 0:
        print("You've run out of guesses, you lose.")
        print(f"The correct number was {number}.")
      else:
        print("Guess again.")
    elif guess < number:
      print("Too low.")
      attempts -= 1
      if attempts == 0:
        print("You've run out of guesses, you lose.")
        print(f"The correct number was {number}.")
      else:
        print("Guess again.")
    elif guess == number:
      print(f"You got it! The number was {guess}.")
      attempts = 0

def guess_the_number():
  print(logo)

  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

  number = random.randint(1,100)           #Generate random number between 1 and 100

  print(f"Pssst, the correct answer is {number}")   #just for testing purposes

  game_running = True

  while game_running is True:
    mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if mode == "easy":
      game_mode(number, mode)
      game_running = False
    elif mode == "hard":
      game_mode(number, mode)
      game_running = False
    else:
      print("Your input is wrong, try again!")

guess_the_number()
while input("Would you like to play again? y to play again: ").lower()=='y':
  #whether user wants to restart the game or not
  clear()
  guess_the_number()
