import random
words = ["hamburger", "cheese", "sushi", "bakery"]
word = random.choice(words)
guessedCorrect = []
guessedWrong = []
currentWord = ""

print("_"*len(word))
print("Welcome to Hangman!")
attemptsLeft = 8

while currentWord != word and attemptsLeft > 0:
    guess = input("\nGuess a letter: ").lower()
    currentWord = ""
    if guess in word:
        guessedCorrect.append(guess)
        for x in word:
            if x in guessedCorrect:
                currentWord += x
            else:
                currentWord += "_"
        print(currentWord)
        print("Correct Guesses:", guessedCorrect)
        print("Wrong Guesses:", guessedWrong)
    else:
        guessedWrong.append(guess)
        attemptsLeft -= 1
        print("Wrong! You have", attemptsLeft, "attempts left.")
        print("Correct Guesses:", guessedCorrect)
        print("Wrong Guesses:", guessedWrong)
if attemptsLeft == 0:
    print("You lose! The word was", word)
else:
    print("You win! The word was", word)


