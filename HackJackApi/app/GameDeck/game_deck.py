import pydealer


class GameDeck:

    def __init__(self, deck_count=6):
        self.deck_count = deck_count
        self.deck = None
        self.reset_deck()

    def reset_deck(self):
        self.deck = pydealer.Deck()
        for i in range(self.deck_count - 1):
            self.deck += pydealer.Deck()

        self.deck.shuffle()

    def deal_cards(self):
        if len(self.deck) == 0:
            self.reset_deck()
        return self.deck.deal(2)

    def hit(self):
        if len(self.deck) == 0:
            self.reset_deck()
        return self.deck.deal(1)











