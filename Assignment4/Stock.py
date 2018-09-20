while True:
    shares = input("Number of shares: ")

    if shares.isalpha():
        print("Invalid number!")
        continue
    else:
        break

while True:
    price = input("Enter a price (dollars, numerator, deniminator): ")
    dollar, nume, denom = price.split(" ")

    if dollar.isalpha() or denom.isalpha() or nume.isalpha():
        print("Invalid Price")
        continue

    else:
        calc = int(dollar) * (int(nume) / int(denom)
        print(shares,"shares with market price " + dollar + " " + nume + "/" + denom + " Have value", calc)

        cont = input("Continue:")

        if cont.upper() == "Y":
            continue
        else:
            break
    