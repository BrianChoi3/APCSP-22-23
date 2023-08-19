
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
CaesarCipher = {}
shift = int(input("How much would you like to shift your Cipher? "))
for letter in letters:
  if shift > 25:
    CaesarCipher.update({letter:letters[shift - 26]})
  else:
    CaesarCipher.update({letter:letters[shift]})
  shift += 1

cont = 1
while cont == 1:
  mode = int(input("\nPick a function:\n \n1. Encrypt\n2. Decrypt\n\nEnter 1 or 2: "))
  if mode == 1:
    phrase = input("Enter a phrase to encrypt: ").lower()
    newPhrase = ""
    for char in phrase:
      if char not in CaesarCipher:
        newPhrase += char
      else:
        newPhrase += CaesarCipher[char]
    print(newPhrase.capitalize())
  elif mode == 2:
    phrase = input("Enter a phrase to decrypt: ").lower()
    newPhrase = ""
    reverseCipher = {}
    for object in list(CaesarCipher.keys()):
      reverseCipher[CaesarCipher[object]] = object
    for char in phrase:
      if char not in reverseCipher:
        newPhrase += char
      else:
        newPhrase += reverseCipher[char]
    print(newPhrase.capitalize())
  cont = int(input("\nEnter 1 to restart, 0 to exit: "))