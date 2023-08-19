toConvert = float(input("How much money do you have? $"))

print("""
Choices:
1: British Pounds
2: Canadian Dollars
3: Chinese Yuan
4: Euros
5: Indian Rupee
6: Japanese Yen
7: Mexican Pesos
8: Norwegian Kroner
9: Swiss Francs
10: Tanzanian Shillings
""")
currency = input("What currency do you want to convert to? ")

if currency == "1":
    print(f"{toConvert * 0.90} British Pounds")
elif currency == "2":
    print(f"{toConvert * 1.37} Canadian Dollars")
elif currency == "3":
    print(f"{toConvert * 7.23} Chinese Yuan")
elif currency == "4":
    print(f"{toConvert * 0.85} Euros")
elif currency == "5":
    print(f"{toConvert * 83.03} Indian Rupee")
elif currency == "6":
    print(f"{toConvert * 110.49} Japanese Yen")
elif currency == "7":
    print(f"{toConvert * 24.24} Mexican Pesos")
elif currency == "8":
    print(f"{toConvert * 10.16} Norwegian Kroner")
elif currency == "9":
    print(f"{toConvert * 0.97} Swiss Francs")
elif currency == "10":
    print(f"{toConvert * 2600.00} Tanzanian Shillings")
else:
    print("Invalid currency")