def create_players_dict(filename):
    the_dict = {}
 
    try:
        filestream = open(filename)
        for line in filestream:
            rank, name, country, rating, byear = line.split(";")
            lastname, firstname = name.split(",")

            key = "{}{}".format(firstname, lastname)
            value_list = [rank, country, rating, byear]
            the_dict[key] = value_list
        filestream.close()
    except FileNotFoundError:
        pass

    return the_dict

def create_countries(dict_players):
    the_dict = {}
    return the_dict

def print_sorted(dict_countries):
    pass   




#   Main Program    #
filename = input("Enter filename: ")
dict_players = create_players_dict(filename)
dict_countries = create_countries(dict_players)
print_sorted(dict_countries)