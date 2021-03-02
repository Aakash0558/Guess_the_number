import random
from art import logo

def easy_mode(number, mode):
  #function for easy mode
  attempts = 10
  while attempts != 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > 100 or guess < 1:
      #for out of bounds guesses
      print("Your guess is out of bounds, you lose one attempt.")
      attempts -= 1
      if attempts == 0:
        print("You've run out of guesses, you lose.")
      else:
        print("Guess again.")
    elif guess > number:
      print("Too high.")
      attempts -= 1
      if attempts == 0:
        print("You've run out of guesses, you lose.")
      else:
        print("Guess again.")
    elif guess < number:
      print("Too low.")
      attempts -= 1
      if attempts == 0:
        print("You've run out of guesses, you lose.")
      else:
        print("Guess again.")
    elif guess == number:
      print(f"You got it! The answer was {guess}.")
      attempts = 0


def hard_mode(number, mode):
  #function for hard mode
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
      else:
        print("Guess again.")
    elif guess > number:
      print("Too high.")
      attempts -= 1
      if attempts == 0:
        print("You've run out of guesses, you lose.")
      else:
        print("Guess again.")
    elif guess < number:
      print("Too low.")
      attempts -= 1
      if attempts == 0:
        print("You've run out of guesses, you lose.")
      else:
        print("Guess again.")
    elif guess == number:
      print(f"You got it! The answer was {guess}.")
      attempts = 0

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1,100)           #Generate random number between 1 and 100

print(f"Pssst, the correct answer is {number}")   #just for testing purposes

game_running = True

while game_running is True:
  mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if mode == "easy":
    easy_mode(number, mode)
    game_running = False
  elif mode == "hard":
    hard_mode(number, mode)
    game_running = False
  else:
    print("Your input is wrong, try again!")
