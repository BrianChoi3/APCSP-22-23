import random
ComputerWinNum = 0
UserWinNum = 0

print("Welcome to Rock, Paper, Scissors!")
playerName = input("What is your name? ")
print(f"Hello {playerName}! Let's play!")
userChoice = input("Rock, Paper, or Scissors? ").lower()

while ComputerWinNum < 3 and UserWinNum < 3:
    computerChoice = random.choice(["rock", "paper", "scissors"])
    if userChoice == computerChoice:
        print("It's a tie!")
    elif userChoice == "rock":
        if computerChoice == "scissors":
            print("You win!")
            UserWinNum += 1
        else:
            print("You lose! The computer chose paper")
            ComputerWinNum += 1


    elif userChoice == "paper":
        if computerChoice == "rock":
            print("You win!")
            UserWinNum += 1
        else:
            print("You lose! The computer chose scissors")
            ComputerWinNum += 1


    elif userChoice == "scissors":
        if computerChoice == "paper":
            print("You win!")
            UserWinNum += 1
        else:
            print("You lose! The computer chose rock.")
            ComputerWinNum += 1
    else:
        print("Invalid input. You lose!")
        ComputerWinNum += 1
    print(f"Score: {playerName} {UserWinNum} - {ComputerWinNum} Computer")
    userChoice = input("Rock, Paper, or Scissors? ").lower()
