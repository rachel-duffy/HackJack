import pytest
import pydealer
from app.PlayBlackJack import play_blackjack


def test_is_bust():
    assert not play_blackjack.is_bust(21)
    assert not play_blackjack.is_bust(10)
    assert play_blackjack.is_bust(23)


def test_get_hard_card_value():
    test_card_1 = pydealer.Card(value="King", suit="Hearts")
    test_card_2 = pydealer.Card(value="7", suit="Spades")
    assert play_blackjack.get_hard_card_value(test_card_1) == 10
    assert play_blackjack.get_hard_card_value(test_card_2) == 7


def test_get_hand_value():
    test_card_king = pydealer.Card(value="King", suit="Hearts")
    test_card_7 = pydealer.Card(value="7", suit="Spades")
    test_card_ace = pydealer.Card(value="Ace", suit="Clubs")
    assert play_blackjack.get_hand_value([test_card_king, test_card_7]) == 17
    assert play_blackjack.get_hand_value([test_card_king, test_card_7, test_card_ace]) == 18
    assert play_blackjack.get_hand_value([test_card_7, test_card_ace, test_card_ace]) == 19
    assert play_blackjack.get_hand_value([test_card_king, test_card_ace, test_card_ace]) == 12
    assert play_blackjack.get_hand_value([test_card_king, test_card_ace, test_card_ace, test_card_7]) == 19
    assert play_blackjack.get_hand_value([test_card_king, test_card_ace]) == 21




