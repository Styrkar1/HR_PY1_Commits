tile = 1.1
while True:
    print(tile)
    if tile == 3.1:
        print("Victory!")
        break
    else:
        if tile == 1.1:
            tule = input("You can travel: (N)orth.\nDirection: ")
            if tule.upper() == "N":
                tile = 1.2
            else:
                print("Not a valid direction!")

        elif tile == 1.2:
            tule = input("You can travel: (N)orth or (E)ast or (S)outh.\nDirection: ")
            if tule.upper() == "N":
                tile = 1.3
            elif tule.upper() == "E":
                tile = 1.1
            elif tule.upper() == "S":
                tile = 1.1
            else:
                print("Not a valid direction!")
            
        elif tile == 1.3:
            tule = input("You can travel:(E)ast or (S)outh.\nDirection: ")
            if tule.upper() == "E":
                tile = 2.3
            elif tule.upper() == "S":
                tile = 1.2
            else:
                print("Not a valid direction!")

        elif tile == 2.1:
            tule = input("You can travel: (N)orth.\nDirection: ")
            if tule.upper() == "N":
                tile = 2.2
            else:
                print("Not a valid direction!")

        elif tile == 2.2:
            tule = input("You can travel: (W)est or (S)outh.\nDirection: ")
            if tule.upper() == "W":
                tile = 1.2
            elif tule.upper() == "S":
                tile = 2.1
            else:
                print("Not a valid direction!")

        elif tile == 2.3:
            tule = input("You can travel: (E)ast or (W)est.\nDirection: ")
            if tule.upper() == "E":
                tile = 3.3
            elif tule.upper() == "W":
                tile = 1.3
            else:
                print("Not a valid direction!")

        elif tile == 3.2:
            tule = input("You can travel: (N)orth or (S)outh.\nDirection: ")
            if tule.upper() == "N":
                tile = 3.3
            elif tule.upper() == "S":
                tile = 3.1
            else:
                print("Not a valid direction!")

        elif tile == 3.3:
            tule = input("You can travel: (W)est or (S)outh.\nDirection: ")
            if tule.upper() == "W":
                tile = 2.3
            elif tule.upper() == "S":
                tile = 3.2
            else:
                print("Not a valid direction!")

        else:
            print("Unknown, Breaking")
            break