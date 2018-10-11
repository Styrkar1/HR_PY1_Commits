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
    

def get_longest_word(words): 
    count = 0
    greatest = 0
    #splits the aquired word so i don't just get individual letters
    words = words.split("\n")
    for line in words:
        #count the number of letters in the word
        count = len(line)
        #if the current count is greater than the greatest count the greatest count becomes the current count
        if count > greatest:
            greatest = count
            #and set the longest word to a variable to return later
            longest = line
    return longest

# The main program starts here
filename = input("Enter name of file: ")
file_stream = open_file(filename)
if file_stream:
	longest_word = get_longest_word(file_stream)
	print("Longest word is '{:s}' of length {:d}".format(longest_word, len(longest_word)))
	#file_stream.close()
else:
	print('File',filename,'not found!')
