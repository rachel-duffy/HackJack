import pytest
import pydealer
from app.GameDeck import game_deck


def test_game_deck_deal_and_hit():
    test_deck = game_deck.GameDeck()
    assert len(test_deck.deck) == 312
    test_deck.deal_cards()
    assert len(test_deck.deck) == 310
    test_deck.hit()
    assert len(test_deck.deck) == 309


def test_game_deck_reshuffles():
    test_deck = game_deck.GameDeck()
    while test_deck.deck.size > 0:
        test_deck.hit()

    test_deck.hit()

    assert test_deck.deck.size == 311

