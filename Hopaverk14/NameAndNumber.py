InMore = "Y"
peoplelist = []
people = {}
count = 0
while InMore.upper() == "Y":
    nam = input("Name: ")
    num = input("Number: ")

    peoplelist.append(nam)
    peoplelist.append(num)
    people.update( {peoplelist: count} )
    peoplelist = []
    count += 1
    InMore = input("More data (y/n)? ")

print(people)