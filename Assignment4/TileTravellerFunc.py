tile = 11
tule = ""
def notvalid():
    global tule
    print("Not a valid direction!")
    tule = input("Direction: ")
def goup():
    global tile
    tile += 1
def godown():
    global tile
    tile -= 1
def goright():
    global tile
    tile += 10
def goleft():
    global tile
    tile -= 10

def tile11():
    global tule
    tule = input("You can travel: (N)orth.\nDirection: ")
    while tile == 11:
        if tule.upper() == "N":
            goup()
        else:
            notvalid()

def tile12():
    global tule
    tule = input("You can travel: (N)orth or (E)ast or (S)outh.\nDirection: ")
    while tile == 12:
        if tule.upper() == "N":
            goup()
        elif tule.upper() == "E":
            goright()
        elif tule.upper() == "S":
            godown()
        else:
            notvalid()

def tile13():
    global tule
    tule = input("You can travel: (E)ast or (S)outh.\nDirection: ")
    while tile == 13:
        if tule.upper() == "E":
            goright()
        elif tule.upper() == "S":
            godown()
        else:
            notvalid()

def tile21():
    global tule
    tule = input("You can travel: (N)orth.\nDirection: ")
    while tile == 21:
        if tule.upper() == "N":
            goup()
        else:
            notvalid()

def tile22():
    global tule
    tule = input("You can travel: (S)outh or (W)est.\nDirection: ")
    while tile == 22:
        if tule.upper() == "W":
            goleft()
        elif tule.upper() == "S":
            godown()
        else:
            notvalid()

def tile23():
    global tule
    tule = input("You can travel: (E)ast or (W)est.\nDirection: ")
    while tile == 23:
        if tule.upper() == "E":
            goright()
        elif tule.upper() == "W":
            goleft()
        else:
            notvalid()

def tile32():
    global tule
    tule = input("You can travel: (N)orth or (S)outh.\nDirection: ")
    while tile == 32:
        if tule.upper() == "N":
            goup()
        elif tule.upper() == "S":
            godown()
        else:
            notvalid()

def tile33():
    global tule
    tule = input("You can travel: (S)outh or (W)est.\nDirection: ")
    while tile == 33:
        if tule.upper() == "W":
            goleft()
        elif tule.upper() == "S":
            godown()
        else:
            notvalid()

def victory():
    print("Victory!")

def broken():
    print("Unknown, Breaking")

while True:
    if tile == 31:
        victory()
        break
    else:
        if tile == 11:
            tile11()

        elif tile == 12:
            tile12()
                
        elif tile == 13:
            tile13()

        elif tile == 21:
            tile21()

        elif tile == 22:
            tile22()

        elif tile == 23:
            tile23()

        elif tile == 32:
            tile32()

        elif tile == 33:
            tile33()
        else:
            broken()
            break
