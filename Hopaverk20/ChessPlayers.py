class chess_player():
    def __init__(self,name,byear,rating):
        self.name = name
        self.byear = byear
        self.rating = rating

def get_highest_rated_player(inp):
    pass

def get_average_rating(ino):
    pass

def main():

    number_of_players = int(input("Number of players: "))
    players = []
    
    print("--- Reading players ---")
    #here you should get info from the user about 
    #number_of_players many chess player
    # code goes here....
    
    print("--- Displaying players --- ")
    #here you should print each player
    #code goes here....

    highest_rated_player = get_highest_rated_player(players)
    print("Highest rated player: ")
    print(highest_rated_player)

    average_rating = get_average_rating(players)
    print("Average rating:", average_rating)

main()