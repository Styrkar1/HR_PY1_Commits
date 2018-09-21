while True:
    while True:
        shares = input("Number of shares: ")

        if shares.isalpha():
            print("Invalid number!")
            continue
        else:
            break

    price = input("Enter a price (dollars, numerator, deniminator): ")
    dollar, nume, denom = price.split(" ")

    if dollar.isalpha() or denom.isalpha() or nume.isalpha():
        print("Invalid Price")
        continue

    else:
        calc = 0.0
        calc = (float(dollar) + (float(nume) / float(denom))) * float(shares)
        print( "%.2f" % calc)
        cont = input("Continue: ")

        if cont.upper() == "Y":
            continue

        else:
            break
