cipher = {"a" : "g", 
         "b" : "x",
         "c" : "a",
         "d" : "m",
         "e" : "l",
         "f" : "r",
         "g" : "w",
         "h" : "q",
         "i" : "v",
         "j" : "h",
         "k" : "j",
         "l" : "b",
         "m" : "c",
         "n" : "f",
         "o" : "u",
         "p" : "y",
         "q" : "e",
         "r" : "z",
         "s" : "o",
         "t" : "p",
         "u" : "n",
         "v" : "d",
         "w" : "i",
         "x" : "t",
         "y" : "s",
         "z" : "k",
         "0" : "5",
         "1" : "7",
         "2" : "4",
         "3" : "6",
         "4" : "0",
         "5" : "8",
         "6" : "3",
         "7" : "1",
         "8" : "9",
         "9" : "2",
         " " : " "}
cont = 1
while cont == 1:
  mode = int(input("\nPick a function:\n \n1. Encrypt\n2. Decrypt\n\nEnter 1 or 2: "))
  if mode == 1:
    phrase = input("Enter a phrase to encrypt: ").lower()
    newPhrase = ""
    for char in phrase:
      if char not in cipher:
        newPhrase += char
      else:
        newPhrase += cipher[char]
    print(newPhrase.capitalize())
  elif mode == 2:
    phrase = input("Enter a phrase to decrypt: ").lower()
    newPhrase = ""
    reverseCipher = {}
    for object in list(cipher.keys()):
      reverseCipher[cipher[object]] = object
    for char in phrase:
      if char not in reverseCipher:
        newPhrase += char
      else:
        newPhrase += reverseCipher[char]
    print(newPhrase.capitalize())
  cont = int(input("\nEnter 1 to restart, 0 to exit: "))