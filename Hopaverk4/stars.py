stars = int(input("Max number of stars: ")) # Do not change this line

for i in range(0, stars):
    if i >= 5:
        for x in range (5,i-1):
            print("*")
    else:
        for j in range(0, i+1):
            print("*")
    print()