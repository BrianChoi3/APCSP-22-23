stones = 20

player1 = input("Player 1, enter your name: ")
player2 = input("Player 2, enter your name: ")

while stones > 0:
    print(f"There are {stones} stones left.")
    stones -= int(input(f"{player1}, how many stones do you want to take (1-3)? "))
    if stones <= 0:
        print(f"{player1} wins!")
        exit()
    print(f"There are {stones} stones left.")
    stones -= int(input(f"{player2}, how many stones do you want to take (1-3)? "))
    if stones <= 0:
        print(f"{player2} wins!")
        exit()