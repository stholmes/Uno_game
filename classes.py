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

    def create_cards(self):
        for color in ["Red", "Yellow", "Blue", "Green"]:
            for i in range(21):
                card = Card(color, i)
                self.deck.append(card)
        shuffle(self.deck)
        shuffle(self.deck)
        return self.deck

    def remove_card(self):
        return self.deck.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __repr__(self):
        return f"{self.name}"

    def draw_card(self, deck):
        new_card = deck.remove_card()
        self.hand.append(new_card)
        return self

    def draw_hand(self, deck):
        for number in range(7):
            self.draw_card(deck)
        return self

    def display_option(self, discard_pile, deck, name):
        print("*" * 50 + f"\n\nPlayer Turn: {name}\n\n")
        print(f"Discard Pile: {discard_pile}\n\nCurrent hand:")
        self.show_hand()
        selection = input(
            "\n\n\n Select action:  #1 - Draw Card     #2 - Play Card\n\n   "
        )

        if selection == "1":
            self.draw_card(deck)
            return self.display_option(discard_pile, deck, name)
        elif selection == "2":
            return self.play_card(discard_pile)
        else:
            print("\n\n*****Invalid action: try again*****\n\n")
            self.display_option(discard_pile, deck, name)

        return self

    def play_card(self, discard_pile):
        print(f"\n\nDiscard Pile: {discard_pile}")
        color = discard_pile.color
        number = discard_pile.number
        self.show_hand()
        card_selection = input("Pick a card to play: ")
        if int(card_selection) > len(self.hand) - 1:
            print(f"\n\n\nInvalid Selection. Selection out of range.")
            return self.play_card(discard_pile)
        selected_card = self.hand[int(card_selection)]
        if selected_card.color == color or selected_card.number == number:
            print("\n\n\n")
            discard_pile = selected_card
            self.hand.pop(int(card_selection))
            print(f"\n\nDiscard Pile: {discard_pile}")
            return discard_pile
        else:
            print(f"\n\n\nInvalid Selection.  Card must be a {color} or {number}")
            return self.play_card(discard_pile)

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
