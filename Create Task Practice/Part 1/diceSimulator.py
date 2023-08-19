import random

def roll_dice(num_rolls, num_dice):
    sum = []
    if num_dice == 0:
        return []
    else:
        for i in range(num_rolls):
            tmp = 0
            for i in range(num_dice):
                tmp += random.randint(1, 6)
            sum.append(tmp)
        return sum

def mean(sumDice):
    return sum(sumDice) / len(sumDice)

def median(sumDice):
    sumDice.sort()
    if len(sumDice) % 2 == 0:
        return (sumDice[len(sumDice) // 2] + sumDice[len(sumDice) // 2 - 1]) / 2
    else:
        return sumDice[len(sumDice) // 2]

def mode(sumDice):
    return max(set(sumDice), key=sumDice.count)

def dice_sim(num_rolls, num_dice):
    sumDice = roll_dice(num_rolls, num_dice)
    if len(sumDice) == 0:
        sumDice.append(0)
    print("The max is: ", max(sumDice))
    print("The min is: ", min(sumDice))
    print("The mean is: ", mean(sumDice))
    print("The median is: ", median(sumDice))
    print("The mode is: ", mode(sumDice))
  
def main():   
    simnum = 1
    # num_dice = int(input("How many dice do you want to roll? "))
    loopAmt = int(input("How many simulations do you want to run? "))
    for i in range(loopAmt):
        if simnum == 1:
            print("\nSimulation #", simnum)
            print("No Dice Were Rolled.")
            simnum += 1
        else:   
            num_rolls = int(input("\nHow many times do you want to roll the dice? "))
            print("\nSimulation #", simnum)
            print("Number of dice rolled: ", (simnum - 1), "Number of rolls: ", num_rolls)
            dice_sim(num_rolls, simnum - 1)
            simnum += 1
        # dice_sim(num_rolls, num_dice)

main()