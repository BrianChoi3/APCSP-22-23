symbols = "`~!@#$%^&*()_+-=[]{}|;':,./<>?"

email = input("What is your email? ")
print(f"You've entered the email: {email}")

if "@" in email and email.count("@") == 1:
    email = email.split("@")
else:
    print("Error: 1 '@' Must Be In Your Email")
    exit()

email.append("@")
for x in email[1]:
    email[2] += x
email.remove(email[1])


if len(email[0]) < 1:
    print("Error: Email Inbox Name Must Be At Least 1 Character")
    exit()
else:
    for x in email[0]:
        if x in symbols:
            print("Error: No Symbols Allowed In Email Inbox Name")
            exit()
        else:
            continue

if email[1].count(".") != 1:
    print("Error: 1 '.' Must Be In Your Email")
    exit()

email[1] = email[1].split(".")
email[1].append(".")
if len(email[1][1]) != 3:
    print("Error: Email Domain Must Be 3 Characters")
    exit()
else:
    for x in email[1][1]:
        email[1][2] += x
    email[1].remove(email[1][1])

if len(email[1][0]) < 2:
    print("Error: Email Domain Name Must Be At Least 1 Character")
    exit()
else:
    for x in email[1][0]:
        if x in symbols:
            if x == "@" and email[1][0].count("@") == 1:
                continue
            else:
                print("Error: No Symbols Allowed In Email Domain Name")
                exit()
        else:
            continue

print("Email Verified")