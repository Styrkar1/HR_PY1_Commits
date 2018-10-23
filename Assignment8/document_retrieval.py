def open_file(filename):
    try:
        word_string = ''
        data_file = open(filename, "r")
        for line in data_file:
            word_string += line
        data_file.close()
    except FileNotFoundError:
        return "None"

    word_string = word_string.split("<NEW DOCUMENT>\n")
    return word_string

def make_dict(wordlist):
    counter = -1
    dic = {}
    for i in wordlist:
        counter += 1
        dic[i] = counter
    #i made this before realizing that only the words and file nums
    #were supposed to be present, but despite this i tried to make it work.
    #needless to say it didn't.
    return dic

def search(srh_key,dict_name):
    #[i for i,x in enumerate(wordlist) if x == srh_key]

    #here i have a matter of not knowing how to assign words and
    #their file numbers into a comprehensive dictionary

    #but not for a lack of trying.
    #i've tried all sorts of methods, from the for loop above to
    #using a bunch of temp lists and strings to try to contain
    #and assign the individual words into the dictionary.

    #the problem with the line below is that it needs the exact string
    #and won't count it. otherwise it would have been a fine tool.
    
    list_values = [ key for key,val in dict_name.items() if val == srh_key ]

    return list_values

def read(val,dict):
    toprint = [dict[i] for i in [val]]
    #when i split word_string i get a massive list within the list
    #and i don't know how to select the specific one i need

    #and when using dictionaries for that matter, i don't know how to
    #select the file based on the value, i've seen a bunch of tutorials
    #on how to get the value with they key but not in reverse

    for i in toprint:
        print(i)

def menu():
    correct = 0
    while correct == 0:
        operation = input("What would you like to do?\n1. Search Documents\n2. Print Document\n3. Quit Program\n")
        #operation was just supposed to keep track of the user input
        #but it would have become redundant.
        operation = int(operation)

        if operation == 1:
            src_word = input("Search Documents: ")
            result = search(src_word, dic_Wordlist)
            print(result)

        elif operation == 2:
            filenum = input("Enter document number: ") 
            read(filenum, dic_Wordlist)

        elif operation == 3:
            print("Exiting Program.")
            quit()
            #quit() is supposed to kill the program in it's tracks
            #but i don't think it works.

        else:
            correct = 0
            print("Invalid Input")
    return operation

filename = input("Document collection: \n")

wordstring = open_file(filename)

if wordstring == "None":
    #simple error handling
    print("Documents not found.")
else:
    dic_Wordlist = make_dict(wordstring)
    ans = menu()
