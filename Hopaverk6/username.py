name = input("Input a name: ")

words = name.split(", ")

fname = words[1]
lname = words[0]
stafur = lname[0].upper()
reallast = lname[1:]
dot = "."


print(fname[0].upper() + dot, stafur + reallast)