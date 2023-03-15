#!/usr/bin/env python


# Generate a random number between 1 and 10
import random
number = random.randint(1, 10)

# Ask the user for a guess
guess = int(input("Guess a number between 1 and 10: "))
# Check if the guess is correct
if guess == number:
    print("You win!")
else:

    # If the guess is wrong, tell them what the correct number was
    print("You lose! The correct number was {}.".format(number))

# Run the program
python hello.py
