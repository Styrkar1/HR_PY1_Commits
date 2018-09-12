numb = int(input("Input an integer: "))
hmm = 0
if numb == 0:
    hmm = 0
else:
    print(numb)

while True:
    if numb == 2 or numb == 1:
        break
    elif numb <= 0:
        break
    else:
        numb = numb - 2
        print(numb)

#wow, i really should just have used a for loop, lmao