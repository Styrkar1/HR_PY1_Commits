def create_players_dict(filename):
    the_dict = {}

    def get_value_list():
        a_list = [None]*NUM_ATTRIBUTES
        a_list[RANK] = int(rank)
        a_list[COUNTRY] = country.strip()
        a_list[RATING] = int(rating)
        a_list[BYEAR] = int(byear)
        return a_list

    try:
        filestream = open(filename)
        for line in filestream:
            rank, name, country, rating, byear = line.split(";")
            lastname, firstname = name.split(",")

            key = "{}{}".format(firstname, lastname).strip()
            value_list = get_value_list()
            value_list = [int(rank), country, int(rating), int(byear)]
            the_dict[key] = value_list
        filestream.close()
    except FileNotFoundError:
        pass

    return the_dict

def create_countries(dict_players):
    the_dict = {}

    for chess_player, chess_player_data in dict_players.items():

        country = chess_player_data[COUNTRY]

        if country in the_dict:
            name_list = the_dict[country]
            name_list.append(chess_player)
        else:
            name_list = [chess_player]
            the_dict[country] = name_list

    return the_dict

def get_average_rating(players, dict_players):
    #ratings = []
    #for player in players:
    #    value_list = dict_players[player]
    #    rating = value_list[RATING]
    #    ratings.append(rating)

    ratings = [ dict_players[players][RATING] for player in players]
    average = sum(ratings)/len(ratings)
    return average


def print_sorted(dict_countries):
    sorted_tuples = sorted(dict_countries.items())
    for country, players in sorted_tuples:
        average = get_average_rating(players,country)
        print("{} ({}) ({:.1f}):".format(country, len(players), average))

        for player in players:
            rating = dict_players[player][RATING]
            print("{:>40}{:>10d}".format(player, rating))
    return 

RANK = 0
COUNTRY = 1
RATING = 2
BYEAR = 3
NUM_ATTRIBUTES = 4



#   Main Program    #
filename = input("Enter filename: ")
dict_players = create_players_dict(filename)
dict_countries = create_countries(dict_players)
print_sorted(dict_countries)