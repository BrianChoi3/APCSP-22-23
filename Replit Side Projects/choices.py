from time import sleep
from random import randint

def ChineseCheckersRoom():
  print("\nYou've made it to the first room: Brian's whimsical Chinese Checkers room. you look around and you see two levers. Which one do you switch?")
  choice = 0
  sleep(1)
  while choice != 1 and choice != 2:
    try:
      choice = int(input("\nEnter 1 for the left lever, 2 for the right lever: "))
      if choice != 1 and choice != 2:
        print("Error: Enter 1 or 2. Try again.")
        continue
    except:
      print("Error: Invalid Input. Try again.")
      continue
  sleep(1)
  if choice == 1:
    print("\nYou flipped the left lever and an army of spiders killed you.")
    ContinueOnDeath()
  elif choice == 2:
    LaundryRoom()

def LaundryRoom():
  print("\nYou've made it to the laundry room where Brian cleans all the good children. You see some magic cat food that supposedly grants you night vision. Will you eat the cat food?")
  choice = 0
  sleep(1)
  while choice != 1 and choice != 2:
    try:
      choice = int(input("\nEnter 1 to eat the cat food, 2 to chuck it across the room: "))
      if choice != 1 and choice != 2:
        print("Error: Enter 1 or 2. Try again.")
        continue
    except:
      print("Error: Invalid Input. Try again.")
      continue
  sleep(1)
  if choice == 1:
    print("\nYou seem to have been duped into having Tide Pods. You now have indigestion, double vision, and can't think clearly.")
    PingPongRoom()
  elif choice == 2:
    print("\nYou avoided some fun sensations.")
    PingPongRoom()

def PingPongRoom():
  print("\nYou've made it to the ping room where Brian goes to play ping pong when he's bored of his SQ3Rs. There is a ping pong robot in the room. Do you want to play a quick match?")
  choice = 0
  sleep(1)
  while choice != 1 and choice != 2:
    try:
      choice = int(input("\nEnter 1 yes, 2 for no: "))
      if choice != 1 and choice != 2:
        print("Error: Enter 1 or 2. Try again.")
        continue
    except:
      print("Error: Invalid Input. Try again.")
      continue
  sleep(1)
  if choice == 1:
    print("\nYou won and recieved a magic cookie that granted you night vision.")
    BasementFridge()
  elif choice == 2:
    print("\nThe robot did not like your cowardly behavior. He served 2 lethal ping pong balls at you. You died.")
    ContinueOnDeath()

def BasementFridge():
  print("\nYou're hungry. Now that you can see in the dark, you found a fridge. You open the fridge and find 16 pounds of smoked salmon. Will you eat the salmon?")
  choice = 0
  sleep(1)
  while choice != 1 and choice != 2:
    try:
      choice = int(input("\nEnter 1 yes, 2 for no: "))
      if choice != 1 and choice != 2:
        print("Error: Enter 1 or 2. Try again.")
        continue
    except:
      print("Error: Invalid Input. Try again.")
      continue
  sleep(1)
  if choice == 1:
    print("\nYou ate the smoked salmon and you're feeling wonderful.")
    SupplyCloset()
  elif choice == 2:
    print("\nBrian found you and sent you back to your cage to do more SQ3Rs. You have been sent back to the first room.")
    ChineseCheckersRoom()

def SupplyCloset():
  print("\nYou walk over to a closet. Will you search the closet?")
  choice = 0
  sleep(1)
  while choice != 1 and choice != 2:
    try:
      choice = int(input("\nEnter 1 yes, 2 for no: "))
      if choice != 1 and choice != 2:
        print("Error: Enter 1 or 2. Try again.")
        continue
    except:
      print("Error: Invalid Input. Try again.")
      continue
  sleep(1)
  if choice == 1:
    print("\nThe closet did not have your notebook, however you did find a key.")
    FoodPantry()
  elif choice == 2:
    print("\nYou choose to walk past the closet.")
    ContinueOnDeath()

def FoodPantry():
  print("\nYou walk around searching for a door to use the key on and you find a locked food pantry. Do you want to try to open it?")
  choice = 0
  sleep(1)
  while choice != 1 and choice != 2:
    try:
      choice = int(input("\nEnter 1 yes, 2 for no: "))
      if choice != 1 and choice != 2:
        print("Error: Enter 1 or 2. Try again.")
        continue
    except:
      print("Error: Invalid Input. Try again.")
      continue
  sleep(1)
  if choice == 1:
    print("\nYou peek inside and see Brian munching on chocloate with your SQ3R notebook on his side.")
    IncapacitateBrian()
  elif choice == 2:
    print("\nYou do not try to open the door. You instead force it down. Brian who was eating chocolate threw your notebook at you. It killed you instantly.")
    ContinueOnDeath()

def IncapacitateBrian():
  print("\nYou decide you're going to take back you notebook. How will you do so?")
  choice = 0
  sleep(1)
  while choice != 1 and choice != 2:
    try:
      choice = int(input("\nEnter 1 to attempt to lure him out with some hamsters, 2 to use a net to trap him: "))
      if choice != 1 and choice != 2:
        print("Error: Enter 1 or 2. Try again.")
        continue
    except:
      print("Error: Invalid Input. Try again.")
      continue
  sleep(1)
  if choice == 1:
    print("\nBrian is intrigued by the chocolate. You reclaim your notebook. You must now escape his basement and out the front door.")
    EscapeTheBasement()
  elif choice == 2:
    print("\nThe net does not trap him. You are sent back to the first room to do your SQ3Rs.")
    ChineseCheckersRoom()

def EscapeTheBasement():
  print("\nYou can now escape the basement. You have two choices: Make a dash for the door or go through one more room. Which do you choose?. Dashing to the door carries a variable survival rate.")
  choice = 0
  sleep(1)
  while choice != 1 and choice != 2:
    try:
      choice = int(input("\nEnter 1 to make a dash for the stairs, 2 to go through one more room: "))
      if choice != 1 and choice != 2:
        print("Error: Enter 1 or 2. Try again.")
        continue
    except:
      print("Error: Invalid Input. Try again.")
      continue
  sleep(1)
  if choice == 1:
    for x in range(5):
      Percent = randint(1, 5)
      print(str(100//Percent) + "%")
      sleep(.5)
    print("\n"+ str(100//Percent) + "% Chance of death")
    ChanceOfDeath = randint(1, Percent)
    if ChanceOfDeath == 1:
      print("You slipped on a banana peel and died.")
      ContinueOnDeath()
    else:
      print("You survived and will continue.")
      EscapeTheHouse()
  elif choice == 2:
    print("\nYou choose to go through one more room")
    BoilerRoom()

def BoilerRoom():
  print("\nYou decide to go through one more room. You find yourself in the boiler room. To make it out of the room, you must fix the boiler by setting the boiler pressure to standard pressure in kPa")
  choice = ""
  sleep(1)
  while choice != "101.3":
    try:
      choice = input("\nEnter standard pressure in kPa: ")
    except:
      print("Error: Invalid Input. Try again.")
      continue
  sleep(1)
  if choice == "101.3":
    print("\nYour knowledge of chemistry is outstanding! You escape the boiler room and make it out of the basement")
    EscapeTheHouse()
  else:
    print("\nWrong answer. The boiler failed and exploded. You were killed instantly.")
    ContinueOnDeath()

def EscapeTheHouse():
  print("\nYou have escaped the basement with your life, but maybe not your sanity. The door is a dash away, but Brian is lurking around ready to catch you. You can once again make a dash for it or you can try to trap Brian and escape. Both have variable rates of success and failing both will result in your capture and return to the basement.")
  choice = 0
  sleep(1)
  while choice != 1 and choice != 2:
    try:
      choice = int(input("\nEnter 1 to dash for the door, 2 to attempt to trap Brian: "))
      if choice != 1 and choice != 2:
        print("Error: Enter 1 or 2. Try again.")
        continue
    except:
      print("Error: Invalid Input. Try again.")
      continue
  sleep(1)
  if choice == 1:
    for x in range(5):
      Percent = randint(1, 5)
      print(str(100//Percent) + "%")
      sleep(.5)
    print("\n"+ str(100//Percent) + "% Chance of failure")
    ChanceOfDeath = randint(1, Percent)
    if ChanceOfDeath == 1:
      print("You were caught. Brian sent you back to the basement.")
      EscapeTheBasement()
    else:
      print("Bad Ending: The police mistook you for Brian. You were tased and arrested.\n \n Thank you for playing. Goodbye.")
      ContinueOnDeath()
  elif choice == 2:
    for x in range(5):
      Percent = randint(1, 5)
      print(str(100//Percent) + "%")
      sleep(.5)
    print("\n"+ str(100//Percent) + "% Chance of failure")
    ChanceOfDeath = randint(1, Percent)
    if ChanceOfDeath == 1:
      print("You were caught. Brian sent you back to the basement.")
      EscapeTheBasement()
    else:
      print("Good Ending: You brought Brian out with you. He was promptly arrested and you escaped mostly unharmed with your notebook. \n \n Thank you for playing. Goodbye.")
      ContinueOnDeath()

def ContinueOnDeath():
  choice = ""
  while choice != "Y" and choice != "N":
    try:
      choice = input("\nEnter Y to restart, N to end: ")
      if choice != "Y" and choice != "N":
        print("Error: Enter Y or N. Try again.")
        continue
    except:
      print("Error: Invalid Input. Try again.")
      continue
  if choice == "Y":
    print("\nYou chose to restart.")
    print("---------------------------[NEW GAME]---------------------------")
    start()
  elif choice == "N":
    print("Thanks for playing. Goodbye.")
    exit()

def start():
  print("\nYou're an unnamed history teacher that works in this building, however you have been captured by student Brian who wants your coveted SQ3R notebook. You must escape his basement and reclaim your notebook.")
  sleep(2)
  ChineseCheckersRoom()

start()