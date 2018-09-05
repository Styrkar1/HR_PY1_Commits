inp = input(str("Enter a sentence: "))

sp = list(inp)
countup = 0
countdown = 0
countdig = 0
countpunk = 0
for i in sp:
    if i.isupper():
        countup = countup + 1
    elif i.islower():
        countdown = countdown + 1
    elif i.isdigit():
        countdig = countdig + 1
    elif i == "," or i == "." or i == '"' or i == "-" or i == "'":
        countpunk = countpunk + 1

print("     Upper case     " + str(countup))
print("     Lower case   " + str(countdown))
print("         Digits     " + str(countdig))
print("    Punctuation     " + str(countpunk))