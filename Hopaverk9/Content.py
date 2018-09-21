fil = open("test.txt", "r")
for i in fil:
    i = i.replace(" ", "")
    print(i.strip("\n"))