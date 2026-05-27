""" Generate a random number between 1 and 20.
The user has maximum 5 attempts to guess it.
Display:
  - "Too high"
  - "Too low"
  - "You won"
  - "Game over".    """


import random

secret = random.randint(1, 20)

attempts = 0

while attempts < 5:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    else:
        print("You won")
        break

if guess != secret:
    print("Game over")
