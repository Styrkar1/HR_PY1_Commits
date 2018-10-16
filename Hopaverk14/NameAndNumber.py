def dict_to_tuple(the_dict):
    dict_list = []
    for key, value in the_dict.items():
        temp = (key,value)
        dict_list.append(temp)
    return dict_list

InMore = "Y"
peoplelist = []
people = {}

while InMore.upper() == "Y":
    nam = input("Name: ")
    num = input("Number: ")

    peoplelist.append(nam)
    peoplelist.append(num)
    people.update( { nam : num} )
    peoplelist = []
    InMore = input("More data (y/n)? ")

thelist = dict_to_tuple(people)

print(sorted(thelist))
