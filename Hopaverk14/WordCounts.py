from collections import Counter
def get_word_list(data_file):
    word_string = ''
    for line in data_file:
        word_string += line
    word_string = word_string.replace(".", "")
    word_string = word_string.replace(",", "")
    word_string = word_string.replace("\n", " ")
    word_string = word_string.split(" ")
    return word_string

def word_list_to_counts(wordlist):
    dictionary = Counter(wordlist)
    return dictionary

def dict_to_tuple(the_dict):
    dict_list = []
    for key, value in the_dict.items():
        temp = (key,value)
        dict_list.append(temp)
    return dict_list

def main():
    filename = input("Name of file: ")
    # Get a file pointer
    fpointer = open(filename)
    # Get a list of words from the file
    word_list = get_word_list(fpointer) 
    # Transform the list to a dictionary of word-count pairs
    word_count_dict = word_list_to_counts(word_list) 
    # Finally, makes a list of tuples from the dictionary
    word_count_tuples = dict_to_tuple(word_count_dict)
    print(sorted(word_count_tuples))

main()

#Kinda broke but kinda not.