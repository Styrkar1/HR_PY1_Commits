def open_file(filename):
    try:
        word_string = ''
        data_file = open(filename, "r")
        for line in data_file:
            word_string += line
        data_file.close()
    except:
        return None

    word_string = word_string.split("<NEW_FILE>")
    return word_string

def menu():
    correct = 0
    while correct == 0:
        operation = input("What would you like to do?\n1. Search Documents\n2. Print Document\n3. Quit Program")

        if operation == 1:
            filename = input("FileName: ")
            correct = 1
            return filename

        elif operation < 0:
            print("Invalid Input")
            continue

        else:
            correct = 1
            return operation

filename = print("Document Collection: ")

wordstring = open_file(filename)

ans = menu()


