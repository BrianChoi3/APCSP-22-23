cont = ""
price = 0.00
ordered = ""
while cont != "done":
    yoQuiero = input("What do you want to eat? pick from: hamburger, pizza, sushi, taco, pasta: ").lower()
    if yoQuiero == "hamburger":
        price += 1.00
        ordered += "hamburger "
    elif yoQuiero == "pizza":
        price += 2.50
        ordered += "pizza "
    elif yoQuiero == "sushi":
        price += 3.00
        ordered += "sushi "
    elif yoQuiero == "taco":
        price += 2.75
        ordered += "taco "
    elif yoQuiero == "pasta":
        price += 5.00
        ordered += "pasta "
    else:
        print("That's not on the list.")
    cont = input("If you are done, type 'done' and press enter. Otherwise, press enter to contine ").lower()
price = format(price, ".2f")
print(f"Your total cost is: ${price}")
print(f"You ordered: {ordered}")