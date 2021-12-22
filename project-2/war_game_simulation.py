import random #will be used for shuffling

#global variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 
        'Ten','Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10,
        'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card():
    '''
    Creates a card object with suit, rank
    Gets value from values global variable
    '''
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank] #referencing global variable values dict

    #to use print on objects of this class
    def __str__(self):
        return self.rank + ' of ' + self.suit



class Deck():
    '''
    Creates a deck of all 52 card instances
    method to shuffle the deck
    mehtod to Deal a card from the deck
    '''
    def __init__(self):
        self.all_cards = []#empty list to hold all card instances
        for suit in suits: #using global variables
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card) #this will append created card object to all cards list

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player():
    '''
    Creates a player instance to play the game
    mathod to remove the top card from the list (index 0)
    methods to add card/cards at the end of the list (index -1)
    '''
    def __init__(self, name):
        self.name = name
        self.all_cards = [] #to hold cards for that player

    def remove_one(self):
        try:
            return self.all_cards.pop(0) # pop(0) to remove from beginning of list
        except:
            print('Not enough cards to remove')

    def add_cards(self, new_cards):
        if type(new_cards) == type([]): #if new_cards is a list
            self.all_cards.extend(new_cards)
        else: #if new_cards is a single card instance
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'

#Game setup

#creating 2 players to play the game
player_one = Player('One')
player_two = Player('Two')

#create a new deck
new_deck = Deck()
new_deck.shuffle()

#split the deck between both players
for x in range(26): #because there are total 52 cards
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

#setting flag game_on = True so that use while loop
game_on = True

#Actual game play
round_num = 0 #counter for number of rounds calculation
while game_on:
    round_num += 1
    print(f'Currently on round {round_num}')

    #check if player is out of cards
    if len(player_one.all_cards) == 0:
        print('Player one out of cards! Player two wins!')
        game_on = False
        break
    
    if len(player_two.all_cards) == 0:
        print('Player two out of cards! Player one wins!')
        game_on = False
        break

    #start a new round
    player_one_cards = [] #player one crads currently in play for this round
    player_one_cards.append(player_one.remove_one())

    player_two_cards = [] #player two crads currently in play for this round
    player_two_cards.append(player_two.remove_one())

    at_war = True #assume war is happening
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            #add both the stack of cards to player one
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            #add both the stack of cards to player one
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False

        else:
            print('WAR!')

            #check if players have enough cards for WAR
            if len(player_one.all_cards) < 5:
                print('Player one unable to declare war')
                print('Player two wins!')
                game_on = False #break out of outer loop
                break #break out of inner loop

            elif len(player_two.all_cards) < 5:
                print('Player two unable to declare war')
                print('Player one wins!')
                game_on = False #break out of outer loop
                break #break out of inner loop

            else:
                for x in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())