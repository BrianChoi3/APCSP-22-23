pennies = int(input("How many pennies do you have? "))*0.01
nickels = int(input("How many nickels do you have? "))*0.05
dimes = int(input("How many dimes do you have? "))*0.10
quarters = int(input("How many quarters do you have? "))*0.25
singleBills = int(input("How many $1 bills do you have? "))*1.00
fiveBills = int(input("How many $5 bills do you have? "))*5.00
tenBills = int(input("How many $10 bills do you have? "))*10.00
twentyBills = int(input("How many $20 bills do you have? "))*20.00
fiftyBills = int(input("How many $50 bills do you have? "))*50.00
hundredBills = int(input("How many $100 bills do you have? "))*100.00
total = pennies + nickels + dimes + quarters + singleBills + fiveBills + tenBills + twentyBills + fiftyBills + hundredBills
print(format(total, ".2f"))
