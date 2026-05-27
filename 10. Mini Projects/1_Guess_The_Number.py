""" Generate a random number between 1 and 10.
The user must guess the number.
Display:
  - "Too high"
  - "Too low"
  - "Correct"
The game continues until the user guesses correctly.  """


import random

secret = random.randint(1, 10)

guess = 0

while guess != secret:
    guess = int(input("Guess the number: "))

    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    else:
        print("Correct")
