from random import shuffle


class Card:
    def __init__(self, color, number):
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

    def show_hand(self):
        for card in range(len(self.hand)):
            print(f"#{(card)}     {self.hand[card]}")
        return self


test = Deck()
test.create_cards()
a = Player("dummy")
a.draw_hand(test).show_hand()

