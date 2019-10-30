from os import system, name
from time import sleep
from classes import Card, Deck, Player

#clear screen function
def screen_clear():
   if name == 'nt':
      _ = system('cls')
   # for mac and linux(here, os.name is 'posix')
   else:
      _ = system('clear')
# print out some text
print('UNO Game\n')
sleep(2)
# now call function we defined above
screen_clear()


#Create deck
deck = Deck()
deck.create_cards()

#set number of players
def players_num():
    print("Enter number of players:")
    x = int(input())
    print("Number of players set to:", x)
    return x

#Create players
num = players_num()

def create_players(num):
    players = []
    print(f"{num} players will be created")
    for i in range(num):
        print("Enter user name:")
        name = input()
        print(f"Iterator = {i}")
        players.append(Player(name))
        players[i].draw_hand(deck)
    return players

players = create_players(num)

for x in range(len(players)):
    print(f"Hand for user {players[x].name}: ")
    players[x].show_hand()

#set pile

pile = deck.remove_card()
print(f"Pile is: {pile}")

print("Now you are ready to play!")

# print("Enter user name:")
# name = input()
# player_1 = Player(name)
# print (f"Player name is {player_1.name}")
