import os.path
def get_csv(file):
    filecon = ""
    if os.path.isfile(file):
        with open(file,'r') as fin:
            filecon = fin.read()
            return filecon
    else:
        print("Cannot find file: " + file)

def seperation(thefile):
    
    return thefile

files = input("Enter filename containing csv data: ")
print("Indicator                        Min                              Max  ")
print("---------------------------------------------------------------------------------------")
seperation(get_csv(files))