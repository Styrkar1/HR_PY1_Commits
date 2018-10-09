import os.path
def get_csv(file):
    filecon = ""
    if os.path.isfile(file):
        with open(file,'r') as fin:
            line = fin.readlines()
            print(line[1])
            filecon = fin.read()
            return filecon
    else:
        print("Cannot find file: " + file)

def seperation(thefile):
    for i in thefile.split(","):
        i = i.strip("N/A")
        i = i.strip("%")
        print(i)
    return thefile

files = input("Enter filename containing csv data: ")
print("Indicator                        Min                              Max  ")
print("---------------------------------------------------------------------------------------")
seperation(get_csv(files))

# I'm stumped, my man, i have no idea how to do this one.
