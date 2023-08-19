symbols = "!@#$%^&*()_+-=<>?/.,;:[]{}|"
uppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercaseLetters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
upperAlphaCount = 0
lowerAlphaCount = 0
symbolCount = 0
numberCount = 0
errorCount = 0

password = input("Enter a password: ")

if " " in password:
    print("No spaces allowed.")
    errorCount += 1

if len(password) < 6 or len(password) > 12:
    print("Password must be bedtwen 6 and 12 characters.")
    errorCount += 1
    
for x in password:
    if x in symbols:
        symbolCount += 1
    elif x in uppercaseLetters:
        upperAlphaCount += 1
    elif x in lowercaseLetters:
        lowerAlphaCount += 1
    elif x in numbers:
        numberCount += 1

if upperAlphaCount == 0:
    print("Password must have at least 1 uppercase letter.")
    errorCount += 1
if lowerAlphaCount == 0:
    print("Password must have at least 1 lowercase letter.")
    errorCount += 1
if symbolCount == 0:
    print("Password must have at least 1 symbol.")
    errorCount += 1
if numberCount == 0:
    print("Password must have at least 1 number.")
    errorCount += 1

if errorCount == 0:
    print("Password is valid.")
else:
    print("Password is invalid.")
