from random import shuffle


class Card:
    def __init__(self, color="blank", number="blank"):
        self.color = color
        self.number = number

    def __repr__(self):
        return f"{self.color} {self.number}"


class Deck:
    def __init__(self):
        self.deck = []

    def create_cards(self): # add player argument to determine number of cards needed
        for color in ["Red", "Yellow", "Blue", "Green"]:
            for i in range(4):
                card = Card(color, i)
                self.deck.append(card)
        shuffle(self.deck)
        shuffle(self.deck)
        return self.deck

    def remove_card(self):
        if len(self.deck) != 0:
            return self.deck.pop()



class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __repr__(self):
        return f"{self.name}"

    def draw_card(self, deck):
        if len(deck.deck) != 0:
            new_card = deck.remove_card()
            self.hand.append(new_card)
        else:
            print("Deck is empty, no more cards")
        return self

    def draw_hand(self, deck):
        for number in range(7):
            self.draw_card(deck)
        return self

    def display_option(self, discard_pile, deck):
        # print("*" * 50 + f"\n\nPlayer Turn: {self.name}\n")
        print(
            "============================\n" +
            "|  " + f"Discard Pile: {discard_pile}  " + "|\n" +
            "============================\n\n\
            Current hand:"
            )
        self.show_hand()
        print(
            "\n\n\
            Enter card # to play that card\n\n\
                  OR\n\n\
            Select action below:\n\n\
            D - Draw Card\n\
            P - Pass\n\
            Q - Quit\n"
        )
        return self.play_card(discard_pile, deck)

    def play_card(self, discard_pile, deck):
        color = discard_pile.color
        number = discard_pile.number

        selection = input("Select Option: ")
        try:
            card_selection = int(selection)
            # print(f"\n\nDiscard Pile: {discard_pile}")
            # self.show_hand()
            # card_selection = input("Pick a card to play: ")
            
            # validate choice if card played
            if int(card_selection) > len(self.hand) - 1:
                print(f"\n\n\nInvalid Selection. Selection out of range.")
                return self.play_card(discard_pile)
            selected_card = self.hand[int(card_selection)]
            if selected_card.color == color or selected_card.number == number:
                print("\n\n\n")
                discard_pile = selected_card
                self.hand.pop(int(card_selection))
                # print(f"\n\nDiscard Pile: {discard_pile}")
                return discard_pile
            else:
                # print ("invalid input")
                print(f"\n\n\nInvalid Selection.  Card must be a {color} or {number}")
                return self.display_option(discard_pile, deck)
        except ValueError:
            # logic for non card options
            if selection.lower() == "d":
                self.draw_card(deck)
                return self.display_option(discard_pile, deck)
            elif selection.lower() == "p":
                return discard_pile
            elif selection.lower() == "q":
                return exit()

            else:
                print("Invalid Selection, try again.")
                return self.display_option(discard_pile, deck)






    def show_hand(self):
        for card in range(len(self.hand)):
            print(f"#{(card)}     {self.hand[card]}")
        return self


# deck = Deck()
# deck.create_cards()
# discard_pile = deck.remove_card()
# print(discard_pile)
# a = Player("Player A")
# b = Player("Player B")
# a.draw_hand(deck)
# b.draw_hand(deck)

# for i in range(10):

#     if i % 2 == 0:
#         player = a
#     else:
#         player = b
#     discard_pile = player.display_option(discard_pile, deck, player.name)
