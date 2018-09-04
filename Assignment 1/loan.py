#Styrkár Blær Styrmirsson
loan = 0.0
payment = 50.0
month = 0
interest = 0.0
totalinterest = 0.0
while loan <= 2500:
    loan = float(input("Input the cost of the item in $: "))
    if loan >= 2500:
        print("If you took that much money out you would never pay it back. \n")
        continue  
    else:
        break

if loan <= 1000:
    while loan != 0:
        month = month + 1
        interest = (loan * 0.015)
        totalinterest = interest + totalinterest
        loan = loan + interest
        loan = loan - payment
        if loan < 0:
            loan = 0
        print("Month: " + str(month) + " Payment: " + str(round(payment, 2)) + " Interest paid: " + str(round(interest, 2)) + " Remaining debt: " + str(round(loan, 2)))
        if (loan + interest) <= payment:
            interest = loan * 0.015
            payment = loan + interest
        if loan == 0:
            print("\nNumber of months: " + str(month))
            print("Total interest paid: " + str(round(totalinterest, 2)))
else:
    while loan != 0:
        month = month + 1
        interest = (loan * 0.02)
        totalinterest = interest + totalinterest
        loan = loan + interest
        loan = loan - payment
        if loan < 0:
            loan = 0
        print("Month: " + str(month) + " Payment: " + str(round(payment, 2)) + " Interest paid: " + str(round(interest, 2)) + " Remaining debt: " + str(round(loan, 2)))
        if (loan + interest) <= payment:
            interest = loan * 0.02
            payment = loan + round(interest, 3)
        if loan == 0:
            print("\nNumber of months: " + str(month))
            print("Total interest paid: " + str(round(totalinterest, 2)))
