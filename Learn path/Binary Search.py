import random
numbers = []
for i in range(1, 101):
    numbers.append(i)
print(numbers)
def binary_search():
    personalGuess = int(input("Enter your guess: "))
    highGuess = 101
    lowGuess = 0
    numGuesses = 0
    while numGuesses != 7:
        print("is your number", numbers[int((len(numbers)/2)-1)], "or above or below? ")
        CPUguess = input("Enter [above], [below], or [correct]:]")
        if CPUguess == "above":
            lowGuess = numbers[int((len(numbers)/2)-1)]
            numbers.clear()
            for i in range(lowGuess + 1, highGuess):
                numbers.append(i)
            numGuesses += 1
        elif CPUguess == "below":
            highGuess = numbers[int((len(numbers)/2)-1)]
            numbers.clear()
            for i in range(lowGuess + 1, highGuess):
                numbers.append(i)
            numGuesses += 1
        elif CPUguess == "correct":
            print("I guessed your number in", numGuesses, "guesses!")
            break
        else:
            print("Please enter a valid response.")
binary_search()