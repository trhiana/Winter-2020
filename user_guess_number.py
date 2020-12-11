# Computer generates a number within a given range
#and user guesses it.

import random

def guess(n):
    random_number = random.randint(1, n)
    guess = 0
    
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {n}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
    print(f"Congrats! You have guessed the number {random_number} correctly!")

guess(10)
