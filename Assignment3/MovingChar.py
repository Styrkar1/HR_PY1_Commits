charloc = int(input("Input a position between 1 and 10: "))
lr = ""
newloc = charloc

while True:
    print("l - for moving left \nr - for moving right \nAny other leter for quitting")
    lr = input("input your choice: ")
    if lr == "r":
        newloc = newloc + 1
        if newloc > 10:
            print("Your number cannot be creater than 10")
            newloc = 10
    elif lr == "l":
        newloc = newloc - 1
        if newloc < 1:
            print("Your number cannot be less than 1")
            newloc = 1
    else:
        break
    print("new position is: ", newloc)