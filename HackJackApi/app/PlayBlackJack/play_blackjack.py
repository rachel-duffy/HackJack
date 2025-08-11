import pydealer
from app.GameDeck import game_deck


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


class PlayBlackJack:
    player_hand = []
    dealer_hand = []
    player_turn = True
    player_bust = False
    dealer_bust = False

    def __init__(self):
        self.game_deck = game_deck.GameDeck()
        self.reset_round()
        self.play()

    def reset_round(self):
        self.player_hand = self.game_deck.deal_cards()
        self.dealer_hand = self.game_deck.deal_cards()
        self.player_turn = True
        self.player_bust = False
        self.dealer_bust = False
        self.play()

    def get_dealer_status(self):
        if self.player_turn:
            print(f'Dealer has a {self.dealer_hand[0].value}')
        else:
            print('Dealer cards:  ')
            for i in range(len(self.dealer_hand)):
                print(self.dealer_hand[i].value)

    def get_player_status(self):
        player_hand_value = get_hand_value(self.player_hand)
        print('Your cards: ')

        for i in range(len(self.player_hand)):
            print(self.player_hand[i].value)

        if self.player_turn:
            print(f'Total card value: {player_hand_value}')

    def play_dealer(self):
        dealer_hand_value = get_hand_value(self.dealer_hand)
        while dealer_hand_value < 17:
            self.dealer_hand += self.game_deck.hit()
            dealer_hand_value = get_hand_value(self.dealer_hand)
        self.dealer_bust = is_bust(dealer_hand_value)

    def player_hit(self):
        self.player_hand += self.game_deck.hit()
        player_value = get_hand_value(self.player_hand)
        self.player_bust = is_bust(player_value)

    def get_winner(self):
        self.get_player_status()
        self.get_dealer_status()
        dealer_value = get_hand_value(self.dealer_hand)
        player_value = get_hand_value(self.player_hand)
        print(f"Final Player value: {player_value}")
        print(f"Final Dealer value: {dealer_value}")

        if self.player_bust:
            print('You bust! Dealer won :(')

        if self.dealer_bust:
            print('The dealer bust! Player won :)')
        
        if dealer_value > player_value and not self.dealer_bust:
            print('Dealer won :(')
            
        elif player_value > dealer_value and not self.player_bust:
            print('Player won :)')
        
        if player_value == dealer_value:
            print('Push!')

        print("*******************NEW*GAME***********************\n")
        self.reset_round()

    def play(self):
        while not self.player_bust:
            self.get_dealer_status()
            self.get_player_status()
            print('Would you like to hit or stand?')
            action = input('Input H or S: ')

            if action == 'H' or action == 'h':
                self.player_hit()
            elif action == 'S' or action == 's':
                self.play_dealer()
                break
            else:
                print("Command unknown, please input H or S.")

        print("*********************GAME*RESULTS********************\n")
        self.player_turn = False
        self.get_winner()
