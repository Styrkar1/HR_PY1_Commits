d1 = int(input("Input first dice: ")) # Do not change this line
d2 = int(input("Input second dice: ")) # Do not change this line

if d1 < 1 or d1 > 6 and d2 < 1 or d2 > 6:
    print("Invalid input")
else:
    if d1 + d2 == 2 or d1 + d2 == 3 or d1 + d2 == 12:
        print("Loser")
    elif d1 + d2 == 7 or d1 + d2 == 11:
        print("Winner")
    else:
        print(d1+d2)
    
