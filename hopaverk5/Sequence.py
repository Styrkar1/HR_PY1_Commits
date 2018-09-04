n = int(input("Enter the length of the sequence: ")) # Do not change this line

num1 = 1
num2 = 2
num3 = 3
total = 0

for i in range (1, n + 1):
    if i == 1:
        print("1")
    elif i == 2:
        print("2")
    elif i == 3:
        print("3")
    else:
        total = num1 + num2 + num3
        print(total)
        num1 = num2
        num2 = num3
        num3 = total