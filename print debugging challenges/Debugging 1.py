# import random library and time library
import random
import time

# generate random integer between 1 and 100
x = random.randInt(1, 100)

# initialize the guess and num_guesses variables
guess = 0
num_guesses = 0

# while loop to keep asking for guesses until guess
while guess != x:
    # ask for guess
    guess = input("Enter a number between 1 and 100")
    # change type of guess from string to integer
guess = int(guess)
# compare guess to x
while guess > x
    print guess, "is too big"
    num_guesses = num_guesses + 1
    if guess < x:
        print(guess, "is too small")
        num_guesses = num_guesses + 1
    else: # guess == x
        print("Correct!")
        num_guesses = num_guesses + 1
        exit()
# tell program to wait 2 seconds before asking again
time.sleep(2)     
# say how many guesses it took to guess correctly after everything is done
print You guessed correctly after " + num_guesses, "number of guesses"