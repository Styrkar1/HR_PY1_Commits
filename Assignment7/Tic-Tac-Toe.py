def tic():
    for i in ticlist:
        print(i,end='')

Dim = input("Input dimension of the board: ")
ticlist = []

for i in range(1,(int(Dim) * int(Dim)) + 1):
    print(i,end=' ')
    ticlist.append(i)
    if i % int(Dim) == 0:
        ticlist.append("\n")
        print("\n")

x_t = True
o_t = False

while True:
    if x_t == True:
        x_t = input("X position: ")
        #ticlist = [w.replace(str(x_t), 'x') for w in ticlist]
        x_t = False
        o_t = True
        tic()

    elif o_t == True:
        o_t = input("O position: ")
        #ticlist[o_t] = "O"
        x_t= True
        o_t = False
        tic()

    else:
        print("You broke it.")
        break
