fil = open("test.txt", "r")
for i in fil:
    i = i.replace(" ", "")
    i = i.replace("\n", "")
    print(i)