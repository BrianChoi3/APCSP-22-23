IntAmount = float(input("What is your measurement amount (a number)? "))
IntUnit = input("""What unit is your measurement in? (singular, lowercase) 
Options: cup, pint, quart, gallon: """)
IntUnit = IntUnit.lower()

if IntUnit == "cup":
    Pint = IntAmount/2
    Quart = IntAmount/4
    Gallon = IntAmount/16  
    print(IntAmount, IntUnit, "is equal to:")
    print(Pint, "Pints")
    print(Quart, "Quarts")
    print(Gallon, "Gallons")

elif IntUnit == "pint":
    Cup = IntAmount*2
    Quart = IntAmount/2
    Gallon = IntAmount/8
    print(IntAmount, IntUnit, "is equal to:")
    print(Cup, "Cups")
    print(Quart, "Quarts")
    print(Gallon, "Gallons")

elif IntUnit == "quart":
    Cup = IntAmount*4
    Pint = IntAmount*2
    Gallon = IntAmount/4
    print(IntAmount, IntUnit, "is equal to:")
    print(Cup, "Cups")
    print(Pint, "Pints")
    print(Gallon, "Gallons")

elif IntUnit == "gallon":
    Cup = IntAmount*16
    Pint = IntAmount*8
    Quart = IntAmount*4
    print(IntAmount, IntUnit, "is equal to:")
    print(Cup, "Cups")
    print(Pint, "Pints")
    print(Quart, "Quarts")

else:
    print("Error | Not a Valid Unit.")