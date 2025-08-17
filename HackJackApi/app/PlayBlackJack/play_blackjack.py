import pydealer
from app.GameDeck import game_deck
from collections import deque

def is_bust(value):
    if value > 21:
        return True
    return False


def get_hard_card_value(card: pydealer.Card):
    if card.value.isdigit():
        return int(card.value)
    else:
        return 10


def get_hand_value(hand: list[pydealer.Card]):
    aces_count = 0
    hand_value = 0

    for i in range(len(hand)):
        if hand[i].value == 'Ace':
            aces_count += 1
        else:
            hand_value += get_hard_card_value(hand[i])

    for i in range(aces_count):
        if hand_value <= 10 and i == aces_count - 1:
            hand_value += 11
        else:
            hand_value += 1

    return hand_value


def hand_to_json(hand: deque):
    card_list = list(hand)
    card_list_json = []
    for card in card_list:
        card_list_json.append({
            "value": card.value,
            "suit": card.suit
        })
    return card_list_json


class PlayBlackJack:
    player_hand = []
    dealer_hand = []
    player_turn = True
    player_bust = False
    dealer_bust = False

    def __init__(self):
        self.game_deck = game_deck.GameDeck()
        self.reset_round()

    def reset_round(self):
        self.player_hand = self.game_deck.deal_cards()
        self.dealer_hand = self.game_deck.deal_cards()
        self.player_turn = True
        self.player_bust = False
        self.dealer_bust = False

    def get_game_status(self):
        viewable_dealer_hand = [self.dealer_hand[0]] if self.player_turn else self.dealer_hand.cards
        game_status = {
            "playerTurn": self.player_turn,
            "dealer": {
                "hand": hand_to_json(viewable_dealer_hand),
                "handValue": get_hand_value(viewable_dealer_hand),
                "isBust": self.dealer_bust,
            },
            "player": {
                "hand": hand_to_json(self.player_hand.cards),
                "handValue": get_hand_value(self.player_hand),
                "isBust": self.player_bust
            },
            "winner": None
        }

        if not self.player_turn:
            game_status["winner"] = self.get_winner()
            self.reset_round()

        return game_status

    def get_winner(self):
        dealer_value = get_hand_value(self.dealer_hand)
        player_value = get_hand_value(self.player_hand)

        if self.dealer_bust or (player_value > dealer_value and not self.player_bust):
            return "Player"

        elif player_value == dealer_value:
            return "Push"

        else:
            return "Dealer"

    def play_dealer(self):
        self.player_turn = False
        dealer_hand_value = get_hand_value(self.dealer_hand)

        while dealer_hand_value < 17:
            self.dealer_hand += self.game_deck.hit()
            dealer_hand_value = get_hand_value(self.dealer_hand)

        self.dealer_bust = is_bust(dealer_hand_value)
        return self.get_game_status()

    def player_hit(self):
        self.player_hand += self.game_deck.hit()
        player_value = get_hand_value(self.player_hand)
        self.player_bust = is_bust(player_value)

        if self.player_bust:
            self.player_turn = False

        return self.get_game_status()
