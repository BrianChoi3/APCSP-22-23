import random
birthdays = []
for y in range(10):
    birthdays.append(str(random.randint(1, 12)) + "/" + str(random.randint(1, 31)))
    y += 1
print("Dates:", birthdays)

def selection_sort():
    newBirthdays = []
    tmp = []
    sort = []
    nbSTR = ""
    for i in birthdays:
        i = i.split("/")
        i[0]=int(i[0])
        i[1]=int(i[1])
        tmp.append(i)
    tmp.sort(key=lambda x: (x[0], x[1]))
    for x in tmp:
        nbSTR += str(x[0]) + "/" + str(x[1]) + ", "
    return nbSTR

def bubble_sort():
    newBirthdays = []
    tmp = []
    sort = []
    nbSTR = ""
    for i in birthdays:
        i = i.split("/")
        i[0]=int(i[0])
        i[1]=int(i[1])
        tmp.append(i)
    tmp.sort(key=lambda x: (x[0], x[1]), reverse=True)
    for x in tmp:
        nbSTR += str(x[0]) + "/" + str(x[1]) + ", "
    return nbSTR

print("Selection Sort:", selection_sort())
print("Bubble Sort:", bubble_sort())