# Constants to be used in the implementation
DIM = 5
POSITION = 'o'
EMPTY = 'x'
LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'
QUIT = 'q'

def get_move():
    ''' Returns a move corresponding to the user input direction '''
    move = input('Move: ')
    
    if move not in [LEFT, RIGHT, UP, DOWN]:
        return QUIT
    else:
        return move

def initialize_grid():
    ''' Returns an initialized grid for the given dimension '''
    grid = []

    for i in range(DIM):
        sublist = []
        for j in range(DIM):
            sublist.append(EMPTY)
        grid.append(sublist)

    grid[0][0] = POSITION  # Current position
    return grid

def print_grid(thegrid):
    pls = thegrid
    for i in pls:
        print("\n")
        for j in i:
            print(j, end = " ")
    print("\n")

def x_ify(thegrid):
    line = -1
    column = -1
    pls = thegrid
    for i in pls:
        column += 1
        line = -1
        for j in i:
            line += 1
            if j == POSITION:
                thegrid[column][line] = EMPTY

def change(thegrid,column,line):
    x_ify(thegrid)
    thegrid[column][line] = POSITION
    print_grid(thegrid)

#print(initialize_grid())
thegrid = initialize_grid()
print_grid(thegrid)
responce = ""
line = 0
column = 0

while responce != QUIT:

    responce = get_move()

    if column > 5:
        column = 0
    if line > 5:
        line = 0

    if responce.lower() == UP:
        column -=1
        change(thegrid,column,line)
    
    if responce.lower() == DOWN:
        column += 1
        change(thegrid,column,line)

    if responce.lower() == LEFT:
        line -= 1
        change(thegrid,column,line)

    if responce.lower() == RIGHT:
        line += 1
        change(thegrid,column,line)