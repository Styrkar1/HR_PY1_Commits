def open_file(filename):
    #Ripped from an old assignment
    try:
        word_string = ''
        data_file = open(filename, "r")
        for line in data_file:
            word_string += line
        data_file.close()
    except:
        return None
    return word_string

def bigrams(words):
    wprev = None
    for w in words:
        yield (wprev, w)
        wprev = w


inp = input("Enter name of the file: ")

wordlist = open_file(inp)
wordlist = wordlist.split(" ")
big = bigrams(wordlist)

for i in big:
    print(i)