from classes import *
from random import shuffle

# initiate game
# make deck, players, discard pile

deck = Deck()
players = shuffle([Player("A"), Player("B"), Player("C")])
pile = "Green 10"



# game turn/continue/end logic

current_player = players[0]
while current_player.hand != None:
    # player turn logic
    current_player = 
    pass


print(f"Glorious victory goes to Player {current_player.name}!")