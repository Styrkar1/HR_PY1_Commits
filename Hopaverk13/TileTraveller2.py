tile = 11
coins = 0
lever = ""
replay = "Y"
while replay == "Y":
    if tile == 31:
        print("Victory!")
        replay = input("Play again (y/n): ")
        replay = replay.upper()
        if replay == "Y":
            coins = 0
            tile = 11
            continue
        else:
            break
    else:
        if tile == 11:
            tule = input("You can travel: (N)orth.\nDirection: ")
            while tile == 11:
                if tule.upper() == "N":
                    tile = 12
                else:
                    print("Not a valid direction!")
                    tule = input("Direction: ")

        elif tile == 12:
            lever = input("Pull a lever (y/n): ")
            if lever.upper() == "Y":
                coins += 1
                print("You received 1 coins, your total is now " + str(coins) + ".")
            tule = input("You can travel: (N)orth or (E)ast or (S)outh.\nDirection: ")
            while tile == 12:
                if tule.upper() == "N":
                    tile = 13
                elif tule.upper() == "E":
                    tile = 22
                elif tule.upper() == "S":
                    tile = 11
                else:
                    print("Not a valid direction!")
                    tule = input("Direction: ")
                
        elif tile == 13:
            tule = input("You can travel: (E)ast or (S)outh.\nDirection: ")
            while tile == 13:
                if tule.upper() == "E":
                    tile = 23
                elif tule.upper() == "S":
                    tile = 12
                else:
                    print("Not a valid direction!")
                    tule = input("Direction: ")

        elif tile == 21:
            tule = input("You can travel: (N)orth.\nDirection: ")
            while tile == 21:
                if tule.upper() == "N":
                    tile = 22
                else:
                    print("Not a valid direction!")
                    tule = input("Direction: ")

        elif tile == 22:
            lever = input("Pull a lever (y/n): ")
            if lever.upper() == "Y":
                coins += 1
                print("You received 1 coins, your total is now " + str(coins) + ".")
            tule = input("You can travel: (S)outh or (W)est.\nDirection: ")
            while tile == 22:
                if tule.upper() == "W":
                    tile = 12
                elif tule.upper() == "S":
                    tile = 21
                else:
                    print("Not a valid direction!")
                    tule = input("Direction: ")

        elif tile == 23:
            lever = input("Pull a lever (y/n): ")
            if lever.upper() == "Y":
                coins += 1
                print("You received 1 coins, your total is now " + str(coins) + ".")
            tule = input("You can travel: (E)ast or (W)est.\nDirection: ")
            while tile == 23:
                if tule.upper() == "E":
                    tile = 33
                elif tule.upper() == "W":
                    tile = 13
                else:
                    print("Not a valid direction!")
                    tule = input("Direction: ")

        elif tile == 32:
            lever = input("Pull a lever (y/n): ")
            if lever.upper() == "Y":
                coins += 1
                print("You received 1 coins, your total is now " + str(coins) + ".")
            tule = input("You can travel: (N)orth or (S)outh.\nDirection: ")
            while tile == 32:
                if tule.upper() == "N":
                    tile = 33
                elif tule.upper() == "S":
                    tile = 31
                else:
                    print("Not a valid direction!")
                    tule = input("Direction: ")

        elif tile == 33:
            tule = input("You can travel: (S)outh or (W)est.\nDirection: ")
            while tile == 33:
                if tule.upper() == "W":
                    tile = 23
                elif tule.upper() == "S":
                    tile = 32
                else:
                    print("Not a valid direction!")
                    tule = input("Direction: ")

        else:
            print("Unknown, Breaking")
            break
