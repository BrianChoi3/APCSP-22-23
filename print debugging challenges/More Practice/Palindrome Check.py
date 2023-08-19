word = input("Enter a word: ")
listWord = list(word) 
newWord = "" 
for char in range(len(listWord)-1,-1,-1): 
  newWord = newWord + word[char] 
print(newWord)

if newWord == word: 
  print("This is a palindrome!")
else:
    print("This is not a palindrome!")