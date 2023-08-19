TopCords = [2,3,4,5,6,7,8,9,10]; SideCords = [1,2,3,4,5,6,7,8,9,10]
for x in SideCords:
    print(x, end="\t")
    for y in TopCords:
        print((x * y), end="\t")
    print("\n")