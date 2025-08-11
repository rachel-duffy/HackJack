import pydealer


class GameDeck:

    def __init__(self, deck_count=6):
        self.deck_count = deck_count
        self.deck = pydealer.Deck(rebuild=True, re_shuffle=True)
        for i in range(deck_count - 1):
            self.deck += pydealer.Deck()
        self.deck.shuffle()

    def deal_cards(self):
        return self.deck.deal(2)

    def hit(self):
        return self.deck.deal(1)











