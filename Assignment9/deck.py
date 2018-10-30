import random
class Card():
    counter = 0
    valid_cards = ["A","J","Q","K"]
    Suits = ["S","H","D","C"]
    Nums = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    def __init__(self,rank=0,suit=""):
        self.rank = rank
        self.suit = suit

    def is_blank(self):
        if self.suit == "" and self.rank == 0:
            return True
        else:
            return False

    def __str__(self):
        #this is my opus magnum.
        #my spaghettius Maximus
        #what it does is check if the values are default (therefor blk) and then it checks if the given values are valid by seeing if they're in a list of valid numbers and letters
        #if the given values are not present in the list of all possible correct values, then blk
        if self.suit == "" and self.rank == 0:
            return "blk"
        else:
            if self.rank in self.Nums or str(self.rank).upper() in self.valid_cards:
                if str(self.suit).upper() in self.Suits:
                    return "{:>2}{}".format(str(self.rank).upper(),str(self.suit).upper())
                else:
                    return "blk"
            else:
                return "blk"

class Deck():
    the_hand = []
    def __init__(self):
        letters = ["S","H","D","C"]
        #at this rate i'll make a count of my counters so i don't lose count of all the counters i have
        counter = 1
        meta_counter = 0
        letter_counter = -1
        space_counter = 0
        for i in range (1,14):
            meta_counter += 1
            letter_counter += 1
            space_counter += 1

            self.the_hand.append(Card(counter,letters[letter_counter]))

            if meta_counter == 4:
                counter +=1

            if letter_counter == 3:
                letter_counter = -1

            if space_counter == 13:
                self.the_hand.append("\n")
                space_counter = 0

    def __str__(self):
        for i in self.the_hand:
            return i

    def shuffle(self):
        random.shuffle(self.the_hand)
        return self.the_hand
    
    def deal(self):
        F_card = self.the_hand[0]
        self.the_hand.pop(0)
        return F_card
        

class PlayingHand():
    NUMBER_CARDS = 13

    def __init__(self):
        pass

    def __str__(self):
        pass

    def add_card(self):
        pass


def test_cards():
    card1 = Card()
    print(card1)
    card2 = Card(5,'s')
    print(card2)
    card3 = Card('Q','D')
    print(card3)
    card4 = Card('x', 7)
    print(card4)

def print_4_hands(hand1, hand2, hand3, hand4):
    ''' Prints the 4 hands '''
    print(hand1)
    print(hand2)
    print(hand3)
    print(hand4)

def deal_4_hands(deck, hand1, hand2, hand3, hand4):
    ''' Deals cards for 4 hands '''
    for i in range(PlayingHand.NUMBER_CARDS):
        hand1.add_card(deck.deal())
        hand2.add_card(deck.deal())
        hand3.add_card(deck.deal())
        hand4.add_card(deck.deal())

def test_hands(deck):
    hand1 = PlayingHand()
    hand2 = PlayingHand()
    hand3 = PlayingHand()
    hand4 = PlayingHand()
    print("The 4 hands:")
    print_4_hands(hand1, hand2, hand3, hand4)
    deal_4_hands(deck, hand1, hand2, hand3, hand4)
    print("The 4 hands after dealing:")
    print_4_hands(hand1, hand2, hand3, hand4)


# The main program starts here

random.seed(10) # i don't know what purpose this random function is supposed to serve, especially since i had to import random to even make it work
test_cards()
deck = Deck()
deck.shuffle()
print("The deck:")
print(deck)
test_hands(deck)
print("The deck after dealing:")
print(deck)