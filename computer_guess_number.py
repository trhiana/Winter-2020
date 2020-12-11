# User provides a number in a given range
# and the computer guesses it

import random

def computer_guess(n):
    lo = 1
    hi = n
    feedback = ""
    while feedback != "c":
        if lo != hi:
            guess = random.randint(lo, hi)
        else:
            guess = lo
                    
        feedback = input(f"Is {guess} too high (h), too low (l) or correct (c)?: ")
        if feedback == "h":
            hi = guess - 1
        elif feedback == "l":
            lo = guess + 1
    print(f"Congrats! The computer guessed your number, {guess}, correctly!")

computer_guess(10)