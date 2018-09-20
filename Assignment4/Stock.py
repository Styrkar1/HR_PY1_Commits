shares = int(input("Number of shares: "))

price = input("Enter a price (dollars, numerator, deniminator): ")

dollar, nume, denom = price.split(" ")

while True:
    print(dollar," ",denom," ", nume)

    try:
        val = str(dollar)
        val = str(nume)
        val = str(denom)
    except ValueError:
        print("Not acceptable")
    break