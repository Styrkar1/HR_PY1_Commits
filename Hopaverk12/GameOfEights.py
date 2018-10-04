def game_of_eights(thelist):
    prevnum = None
    Newnum = None

    for prevnum,Newnum in zip(thelist[::],thelist[1::]):
        if prevnum.isalpha() or Newnum.isalpha():
            return "Error. Please enter only integers."

    for prevnum,Newnum in zip(thelist[::],thelist[1::]):
        if prevnum == Newnum:
            return True
# not quite right since it's only supposed to be true whe newnum and prevnum are both 8
    return False

def main():
    a_list = input("Enter elements of list separated by commas: ").split(',')
    print(game_of_eights(a_list))

main()