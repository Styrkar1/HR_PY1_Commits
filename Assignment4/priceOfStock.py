while True:
    while True:
        try:
            shares = int(input("Enter number of shares: "))

        except ValueError:
            print("Invalid number!")
            continue
        else:
            break
    while True:
        price = input("Enter price (dollars, numerator, denominator): ")
        dollar, nume, denom = price.split(" ")

        if dollar.isalpha() or denom.isalpha() or nume.isalpha():
            print("Invalid price!")
            continue

        else:
            calc = (float(dollar) + (float(nume) / float(denom))) * float(shares)
            calc = "%.2f" % calc
            print(str(shares) + " shares with market price " + str(dollar) + " " + str(nume) + "/" + str(denom) + " have value $" + str(calc))
            break

    cont = input("Continue: ")

    if cont.upper() == "Y":
        continue

    else:
        break
