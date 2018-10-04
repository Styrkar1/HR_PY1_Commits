def build_wordlist(infile):
    wordlist = []
    for line in infile:
        line = line.strip("\n")
        line = line.split(" ")
        if line == " ":
            wordlist.append(line)
        else:
            wordlist.extend(line)
    return wordlist

def find_unique(uniq):
    unique_list = []
    for i in uniq:
        if not i in unique_list:
            unique_list.append(i)
    return unique_list

def main():
    infile = open("test.txt", 'r')
    word_list = build_wordlist(infile)  
    infile.close()  
    new_wordlist = find_unique(word_list)
    new_wordlist.sort()
    print(new_wordlist)

main()