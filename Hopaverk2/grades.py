grade = float(input("Input a grade: "))

if grade >= 5:
    if grade <= 10:
        print("Passing grade!")
    else:
        print("Invalid grade!")
else:
    print("Failing grade!")
