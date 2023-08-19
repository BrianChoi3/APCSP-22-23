symbols = "!@#$%^&*()_+-=<>?/.,;:[]{}|"
uppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercaseLetters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
alnumCount = 0
symbolCount = 0
numberCount = 0

password = input("Enter a crusty password: ")

if " " in password:
    print("No spaces allowed.")
    exit()
elif len(password) < 8:
    print("Password must be at least 8 characters.")
    exit()
elif "password" in password.lower():
    print("Really? That's your password?")
    exit()
else:
    for char in password:
        if char in symbols:
            symbolCount += 1
        elif char in uppercaseLetters:
            alnumCount += 1
        elif char in lowercaseLetters:
            alnumCount += 1
        elif char in numbers:
            numberCount += 1
    if len(password) >= 8 and symbolCount == 0 and numberCount == 0:
        print("Very Weak")
    elif len(password) >= 8 and (symbolCount >= 0 and numberCount == 0) or (symbolCount == 0 and numberCount >= 0):
        print("Weak")
    elif len(password) >= 8 and symbolCount >= 2 or numberCount >= 2:
        print("Strong")
    elif len(password) >= 8 and symbolCount >= 3 or numberCount >= 3:
        print("Very Strong")
    else:
        print("Couldn't determine the strength of the password.")

print(""" 
Criteria for password strength:

Very Weak: 8 or more characters, no symbols or numbers
#
Weak: 8 or more characters, 1 symbol or number
#
Strong: 8 or more characters, at least 2 symbols and 2 numbers
#
Very Strong: 8 or more characters, at least 3 symbols and 3 numbers
""")
    