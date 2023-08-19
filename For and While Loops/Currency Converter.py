toConvert = float(input("How much money do you have? $"))

print("""
Choices:
1: Euros
2: Canadian Dollar
3: Indian Rupee
4: Japanese Yen
5: Vietnamese Dong
6: Korean Won
7: Bitcoin (Fake Money)
8: United States Dollars
""")
validInputs = ["1", "2", "3", "4", "5", "6", "7", "8"]
currency = input("What currency do you want to convert from? ")
while currency not in validInputs:
    print("Error | Not a valid currency.")
    currency = input("What currency do you want to convert from? ")

if currency == "1":
    toConvert = toConvert / 0.81
elif currency == "2":
    toConvert = toConvert / 1.29
elif currency == "3":
    toConvert = toConvert / 65.2
elif currency == "4":
    toConvert = toConvert / 105.75
elif currency == "5":
    toConvert = toConvert / 22750
elif currency == "6":
    toConvert = toConvert / 1079.43 
elif currency == "7":
    toConvert = toConvert / 0.000088
elif currency == "8":
    toConvert = toConvert
else:
    print("Invalid currency") 
    exit()

print("""
Choices:
1: Euros
2: Canadian Dollar
3: Indian Rupee
4: Japanese Yen
5: Vietnamese Dong
6: Korean Won
7: Bitcoin (Fake Money)
8: United States Dollars
""")
validInputs = ["1", "2", "3", "4", "5", "6", "7", "8"]
currency = input("What currency do you want to convert to? ")
while currency not in validInputs:
    print("Error | Not a valid currency.")
    currency = input("What currency do you want to convert to? ")

if currency == "1":
    toConvert = toConvert * 0.81
elif currency == "2":
    toConvert = toConvert * 1.29
elif currency == "3":
    toConvert = toConvert * 65.2
elif currency == "4":
    toConvert = toConvert * 105.75
elif currency == "5":
    toConvert = toConvert * 22750
elif currency == "6":
    toConvert = toConvert * 1079.43
elif currency == "7":
    toConvert = toConvert * 0.000088
elif currency == "8":
    toConvert = toConvert
else:
    print("Invalid currency") 
    exit()

if currency == "1":
    a = "Euros"
elif currency == "2":
    a = "Canadian Dollars"
elif currency == "3":
    a = "Indian Rupee"
elif currency == "4":
    a = "Japanese Yen"
elif currency == "5":
    a = "Vietnamese Dong"
elif currency == "6":
    a = "Korean Won"
elif currency == "7":
    a = "Bitcoin"
elif currency == "8":
    a = "United States Dollars"
else:
    print("Invalid currency") 
    exit()

print(format(toConvert, ".2f"), a)