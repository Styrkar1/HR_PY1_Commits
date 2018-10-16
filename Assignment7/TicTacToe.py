def tic(num,xy):
    newlist = []
    for i in ticlist:
        if i == num:
            newlist.append(xy)
        else:
            newlist.append(i)

    for i in newlist:
        print(i,end='')
    return newlist


def win(board):
    for i in range(0,):
        print(i)


Dim = input("Input dimension of the board: ")
ticlist = []

for i in range(1,(int(Dim) * int(Dim)) + 1):
    print(i,end=' ')
    ticlist.append(i)
    if i % int(Dim) == 0:
        ticlist.append("\n")
        print("\n")

turn = "x"

while turn != "N":
    if turn == "x":
        x_inp = input("X position: ")
        turn = "o"
        ticlist = tic(int(x_inp), "X")
        print(win(ticlist))

    elif turn == "o":
        o_inp = input("O position: ")
        turn = "x"
        ticlist = tic(int(o_inp), "O")
        win(ticlist)

    else:
        print("You broke it.")
        turn = "N"
