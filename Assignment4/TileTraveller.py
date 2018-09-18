tile = 1.1
while True:
    if tile == 3.1:
        print("Victory!")
        break
    else:
        if tile == 1.1:
            tule = input("You can travel: (N)orth")
            if tule.upper() == "N":
                print("Direction: N")
                tile = 1.2
            else:
                print("Not a valid direction!")

        elif tile == 1.2:
            tule = input("You can travel: (N)orth or (E)ast or (S)outh")
            if tule.upper() == "N"
                print("Direction: N")
                tile = 1.3
            elif tule.upper() == "E":
                print("Direction: S")
                tile = 1.1
            
            
        elif tile == 1.3:
            tule = input("You can travel:(E)ast or (S)outh")
            if tule.upper() == "E"
                print("Direction: E")
                tile = 2.3
            elif tule.uppet == "S"
                print("Direction:S")
                tile = 1.2

        elif tile == 2.1:
            tule = input("You can travel: (N)orth")
            if tule.upper() == "N":
                print("Direction: N")
                tile = 2.2

        elif tile == 2.2:
            tule = input("You can travel: (W)est or (S)outh")
            if tule.upper() == "W":
                print("Direction: W")
                tile = 1.2
            elif tule.upper() == "S":
                print("Direction: S")
                tile = 2.1

        elif tile == 2.3:
            tule = input("You can travel: (E)ast or (W)est")
            if tule.upper == "E":
                print("Direction: E")
                tile = 3.3
            elif tule.upper() == "W":
                print("Direction: W")
                tile = 1.3

        elif tile == 3.2:
            tule = input("You can travel: (N)orth or (S)outh")
            if tule.upper() == "N":
                print("Direction: N")
                tile = 3.3
            if tule.upper() == "S":
                print("Direction: S")
                tile = 3.1

        elif tile == 3.3:
            tule = input("You can travel: (W)est or (S)outh")
            if tule.upper() == "W":
                print("Direction: W")
                tile = 2.3
            elif tule.upper() = "S":
                print("Direction: S")
                tile = 3.2

        else:
            print("Unknown, Breaking")
            break