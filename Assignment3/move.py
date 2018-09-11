charloc = int(input("Input a position between 1 and 10: "))
lr = ""
newloc = charloc

def intro():
    global lr
    print("l - for moving left\nr - for moving right\nAny other letter for quitting")
    lr = input("Input your choice: ")

def increase():
    global newloc
    newloc = newloc + 1
    if newloc > 10:
        newloc = 10

def decrease():
    global newloc
    newloc = newloc - 1
    if newloc < 1:
        newloc = 1

def newpos():
    print("New position is:", newloc)

while True:
    intro()

    if lr == "r":
        increase()

    elif lr == "l":
        decrease()

    else:
        break
    newpos()
newpos()
