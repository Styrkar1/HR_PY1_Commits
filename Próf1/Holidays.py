month = input("Month: ")
day = input("Day: ")

fletter = month[0]
moth = month[1:]

combined = fletter.upper() + "" + moth

if combined == "January" and day == "1":
    print("New year's day")

elif combined == "June" and day == "17":
    print("National Holiday")

elif combined == "December" and day == "25":
    print("Christmas day")

else:
    print("Not a holiday")