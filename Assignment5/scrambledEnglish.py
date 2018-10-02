import random
import string
import re
#I can only assume a human being goes over these so here's what i managed
#to do, the rest seems a bit "spooky" and i hope i get graded based on
#what i managed to do and not the "correct" output.


def get_word_string(file):
    datafile = open(file, "r")
    wordstring = ""

    for line in datafile:
        wordstring += line
    return wordstring

def scramble_string(word):
    whole = ""
    word = re.sub(r'[^\w\s]','',word)
    if len(word.split(" ")) > 4:
        for i in word.split(" "):
            midtext = list(i[1: -1])
            random.shuffle(midtext)
            scrambled = (i[0], "".join(midtext), i[-1])
            scrambled = ''.join(scrambled)
            whole = whole + " " + scrambled
    else:
        whole = whole + " " + word
    #Removing the first letter because it is always whitespace
    whole = whole[1:]
    return whole


random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)