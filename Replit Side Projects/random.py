from random import randint
answer = randint(0, 30)
attempt = 0
# print(answer) # for debugging purposes only
while attempt < 5:
    guess = int(input("Give me a number between 0 and 30: "))
    if guess > 30 or guess < 0:
        print("Guess out of range.")
    else:
        if guess == answer:
            print("You win!")
            exit()
        elif guess < answer:
            print("Higher.")
        elif guess > answer:
            print("Lower.")
        else:
            print("An error occurred.")
    attempt += 1
print("Out of Guesses. You lose.")
