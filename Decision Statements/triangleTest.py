SideOne = input("What is the measurement of your first side? ")
SideTwo = input("What is the measurement of your second side? ")
SideThree = input("What is the measurement of your third side? ")

for x in SideOne:
    if x.isalpha():
        SideOne = 1
        break
for x in SideTwo:
    if x.isalpha():
        SideTwo = 1
        break
for x in SideThree:
    if x.isalpha():
        SideThree = 1
        break

SideOne = float(SideOne)
SideTwo = float(SideTwo)
SideThree = float(SideThree)
if (SideOne+SideTwo <= SideThree) or (SideOne+SideThree <= SideTwo) or (SideTwo+SideThree <= SideOne):
    print("Not a triangle")

elif (SideOne == SideTwo) and (SideTwo == SideThree):
    print("Equilateral Triangle")

elif ((SideOne == SideTwo) and (SideTwo != SideThree)) or ((SideThree == SideTwo) and (SideTwo != SideOne)) or ((SideThree == SideOne) and (SideOne != SideTwo)):
    print("Isosceles Triangle")

elif (SideOne != SideTwo and SideTwo != SideThree and SideThree !=  SideOne):
    print("Scalene Triangle")