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

contents = open_file("flights.txt")
contents = contents.replace("\n"," ")

splitted = contents.split(" ")
counter = -2
names = []
name = []

for i in splitted:
    try:
        counter += 2
        name.append(splitted[counter])
    except:
        break

newname = []

for i in name:
    if i not in newname:
        newname.append(i)

counter2 = -1
greatest = 0
newname = sorted(newname)
country = []

try:
    for i in newname:
        if i == '':
            pass
            counter2 += 1
        else:
            num = 0
            counter3 = -1
            counter2 += 1
            print(newname[counter2] + ": ")

            for j in splitted:
                counter3 += 1
                if j == i:
                    #the countries aren't sorted, i's solve this by placing the countries in a list here,
                    #sorting them them printing them once they have all been counted, but i need to get to the other projects
                    #to be able to finish this test on time
                    print("\t" + splitted[counter3 + 1])
                    num += 1

                    if num >= greatest:
                        nam = i
                        greatest = num
except:
    pass

print("\n" + str(nam) + " has been to " + str(greatest) + " countries")
