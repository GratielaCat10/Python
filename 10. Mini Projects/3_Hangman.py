""" The user must guess a hidden word letter by letter.  """

word = "python"

guessed = ""

attempts = 6

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print(display)

    if display == word:
        print("You won")
        break

    char = input("Enter a letter: ")

    if char in word:
        guessed += char
    else:
        attempts -= 1
        print("Wrong letter")

if attempts == 0:
    print("You lost")
  
