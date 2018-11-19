ins = 0.0
chg = 1.50
while ins < 1.50:
    print("A packet of candy costs $ 1.50. You have inserted $ " + "%.2f" % ins + ".")
    print("Please insert coins:")
    inp = input("	n - Nickel\n	d - Dime\n	q - Quarter\n	D - Dollar\n")
    if inp == "n":
        ins += 0.05
    elif inp == "d":
        ins += 0.10
    elif inp == "q":
        ins += 0.25
    elif inp == "D":
        ins += 1.00
    else:
        print("'" + inp + "'" " is not a valid coin.")

leftover = ins - chg
leftover = "%.2f" % leftover
print("Enjoy your candies. Your change is $ " + str(leftover) + ". Please visit again.")

