grossIncome = 0
netIncome = 0
monthly = 0
expenses = 0

nyStateIncomeTaxBracket = [8500, 11700, 13900, 80650, 215400, 1077550, 5000000, 25000000]
federalIncomeTaxBracket = [10275, 41775, 89075, 170050, 215950, 539900]


def budgetCalc():
    print("Yas queen, let's get to budgeting.")
    grossIncome = float(input("What is your annual gross income? "))
    if grossIncome == 0:
        print("Get a job and a grip of your life bro.")
        exit()
    else:
        monthly = float(taxCalc(grossIncome))
    
    print("\nNow, let's calculate your expenses. Enter them all as monthly amounts.")

    monthly -= float(input("\nHow much do you spend on food? "))

    ownHome = input("Do you rent/own a home? (yas/naur) ")
    if ownHome == "yas":
        monthly -= float(input("How much do you spend on rent/mortgage? "))
        monthly -= float(input("How much do you spend on home owners/renters insurance? "))
        monthly -= float(input("How much do you spend on home maintenance? "))
    elif ownHome == "naur":
        pass

    ownCar = input("Do you own a car? (yas/naur) ")
    if ownCar == "yas":
        payingForCar = input("Are you paying off/for the car? (yas/naur) ")
        if payingForCar == "yas":
            monthly -= float(input("How much do you spend on car payments/lease? "))
        elif payingForCar == "naur":
            pass
        monthly -= float(input("How much do you spend on car insurance? "))
        monthly -= float(input("How much do you spend on car maintenance? "))
        monthly -= float(input("How much do you spend on gas? "))
    elif ownCar == "naur":
        usePT = input("Do you use public transportation? (yas/naur) ")
        if usePT == "yas":
            monthly -= float(input("How much do you spend on public transportation? "))
        elif usePT == "naur":
            pass
        
    monthly -= float(input("How much do you spend on utilities? (Heating, Electricity, Water) "))

    monthly -= float(input("How much do you spend on entertainment? (Streaming Services, Cable, Movie Tickets, etc.) "))

    monthly -= float(input("How much do you spend on clothing? "))

    monthly -= float(input("How much do you spend on personal care? (Haircuts, Shampoo, gym memberships, etc.) "))

    monthly -= float(input("How much do you spend on miscellaneous? (Gifts, Donations, etc.) "))

    ownPets = input("Do you own any pets? (yas/naur) ")
    if ownPets == "yas":
        monthly -= float(input("How much do you spend on pet food? "))
        monthly -= float(input("How much do you spend on pet care? (Vet Visits, Pet Insurance, etc.) "))
    else:
        pass
    haveDebt = input("Do you have any debt? (yas/naur) ")
    if haveDebt == "yas":
        monthly -= float(input("How much do you spend on debt payments? (Credit Cards, Student Loans, etc.) "))
    else:
        pass

    monthly -= float(input("How much do you spend on other uncategorized purchases? "))

    print(f"Queen, your net income is ${monthly} per month.")



def taxCalc(grossIncome):
    print("\nqueen, the government is gonna take some of your money through taxes.")
    print("\nluckily, i will calculate the amount for you!")
    print("\nfirst, we will calculate your federal income tax.")
    print(f"\nyou made ${grossIncome} this year.")
    netIncome = grossIncome
    if (grossIncome <= federalIncomeTaxBracket[0]):
        netIncome -= grossIncome * 0.10
    elif (federalIncomeTaxBracket[0] < grossIncome) and (grossIncome <= federalIncomeTaxBracket[1]):
        netIncome -= (1027.50 + (grossIncome - 10275) * 0.12)
    elif (federalIncomeTaxBracket[1] < grossIncome) and (grossIncome <= federalIncomeTaxBracket[2]):
        netIncome -= (4807.50 + (grossIncome - 41775) * 0.22)
    elif (federalIncomeTaxBracket[2] < grossIncome) and (grossIncome <= federalIncomeTaxBracket[3]):
        netIncome -= (15213.50 + (grossIncome - 89075) * 0.24)
    elif (federalIncomeTaxBracket[3] < grossIncome) and (grossIncome <= federalIncomeTaxBracket[4]):
        netIncome -= (34647.50 + (grossIncome - 170050) * 0.32)
    elif (federalIncomeTaxBracket[4] < grossIncome) and (grossIncome <= federalIncomeTaxBracket[5]):
        netIncome -= (49335.50 + (grossIncome - 215950) * 0.35)
    elif (federalIncomeTaxBracket[5] < grossIncome):
        netIncome -= (162718 + (grossIncome - 539900) * 0.37)
    print(f"\nSlayer, after federal income tax, you made ${netIncome} this year.")
    print("\nnow, we will calculate your state income tax.")
    if (grossIncome <= nyStateIncomeTaxBracket[0]):
        netIncome -= grossIncome * 0.04
    elif (nyStateIncomeTaxBracket[0] < grossIncome) and (grossIncome <= nyStateIncomeTaxBracket[1]):
        netIncome -= (340 + (grossIncome - 8500) * 0.045)
    elif (nyStateIncomeTaxBracket[1] < grossIncome) and (grossIncome <= nyStateIncomeTaxBracket[2]):
        netIncome -= (484 + (grossIncome - 11700) * 0.0525)
    elif (nyStateIncomeTaxBracket[2] < grossIncome) and (grossIncome <= nyStateIncomeTaxBracket[3]):
        netIncome -= (600 + (grossIncome - 13900) * 0.0585)
    elif (nyStateIncomeTaxBracket[3] < grossIncome) and (grossIncome <= nyStateIncomeTaxBracket[4]):
        netIncome -= (4504 + (grossIncome - 80650) * 0.0625)
    elif (nyStateIncomeTaxBracket[4] < grossIncome) and (grossIncome <= nyStateIncomeTaxBracket[5]):
        netIncome -= (12926 + (grossIncome - 215400) * 0.0685)
    elif (nyStateIncomeTaxBracket[5] < grossIncome) and (grossIncome <= nyStateIncomeTaxBracket[6]):
        netIncome -= (71984 + (grossIncome - 1077550) * 0.0965)
    elif (nyStateIncomeTaxBracket[6] < grossIncome) and (grossIncome <= nyStateIncomeTaxBracket[7]):
        netIncome -= (450500 + (grossIncome - 5000000) * 0.1030)
    elif (nyStateIncomeTaxBracket[7] < grossIncome):
        netIncome -= (2510500 + (grossIncome - 25000000) * 0.1065)
    print(f"\nSlayer, after state and federal income tax, you made ${netIncome} this year.")
    print("\nnow, we will calculate your social security tax.")
    netIncome -= grossIncome * 0.062
    print(f"\nSlayer, after social security tax, you made ${netIncome} this year.")
    print("\nnow, we will calculate your monthly income.")
    monthly = format((netIncome / 12), ".2f")
    print(f"\nSlayer, after taxes, you make ${monthly} a month.")
    return monthly




def main():
    print("is time to budget season? (yas/naur): ")
    budgetSeason = input()
    if budgetSeason == "yas":
        budgetCalc()
    elif budgetSeason == "naur":
        print("Goodbye.")
        exit()
    else:
        print("is time to budget season? (yas/naur): ")
        budgetSeason = input() 

main()