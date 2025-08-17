import pytest
import pydealer
from app.PlayBlackJack import play_blackjack
from unittest.mock import patch, Mock

test_card_king = pydealer.Card(value="King", suit="Hearts")
test_card_7 = pydealer.Card(value="7", suit="Spades")
test_card_5 = pydealer.Card(value="5", suit="Spades")
test_card_ace = pydealer.Card(value="Ace", suit="Clubs")


def test_is_bust():
    assert not play_blackjack.is_bust(21)
    assert not play_blackjack.is_bust(10)
    assert play_blackjack.is_bust(23)


def test_get_hard_card_value():
    assert play_blackjack.get_hard_card_value(test_card_king) == 10
    assert play_blackjack.get_hard_card_value(test_card_7) == 7


def test_get_hand_value():
    assert play_blackjack.get_hand_value([test_card_king, test_card_7]) == 17
    assert play_blackjack.get_hand_value([test_card_king, test_card_7, test_card_ace]) == 18
    assert play_blackjack.get_hand_value([test_card_7, test_card_ace, test_card_ace]) == 19
    assert play_blackjack.get_hand_value([test_card_king, test_card_ace, test_card_ace]) == 12
    assert play_blackjack.get_hand_value([test_card_king, test_card_ace, test_card_ace, test_card_7]) == 19
    assert play_blackjack.get_hand_value([test_card_king, test_card_ace]) == 21


def test_hand_to_json():
    test_stack = pydealer.Stack()
    test_stack.insert(test_card_king)
    test_stack.insert(test_card_7)
    assert play_blackjack.hand_to_json(test_stack.cards) == [
        {"value": "King", "suit": "Hearts"},
        {"value": "7", "suit": "Spades"},
    ]


def test_start_blackjack_game_player_winner():
    with patch('app.GameDeck.game_deck.GameDeck') as MockGameDeck:
        mock_game_deck = Mock()
        mock_game_deck.deal_cards.return_value = pydealer.Stack(cards=[test_card_7, test_card_king])
        mock_game_deck.hit.return_value = pydealer.Stack(cards=[test_card_ace])
        MockGameDeck.return_value = mock_game_deck

        test_blackjack_game = play_blackjack.PlayBlackJack()
        assert test_blackjack_game.get_game_status() == {
            "playerTurn": True,
            "dealer": {
                "hand": [
                    {
                        'suit': 'Spades',
                        'value': '7'
                    }
                ],
                "handValue": 7,
                "isBust": False,
            },
            "player": {
                "hand": [
                    {
                        'suit': 'Spades',
                        'value': '7'
                    },
                    {
                        'suit': 'Hearts',
                        'value': 'King'
                    }
                ],
                "handValue": 17,
                "isBust": False
            },
            "winner": None
        }

        assert test_blackjack_game.player_hit() == {
            "playerTurn": True,
            "dealer": {
                "hand": [
                    {
                        'suit': 'Spades',
                        'value': '7'
                    }
                ],
                "handValue": 7,
                "isBust": False,
            },
            "player": {
                "hand": [
                    {
                        'suit': 'Spades',
                        'value': '7'
                    },
                    {
                        'suit': 'Hearts',
                        'value': 'King'
                    },
                    {
                        'suit': 'Clubs',
                        'value': 'Ace'
                    }
                ],
                "handValue": 18,
                "isBust": False
            },
            "winner": None
        }

        assert test_blackjack_game.play_dealer() == {
            "playerTurn": False,
            "dealer": {
                "hand": [
                    {
                        'suit': 'Spades',
                        'value': '7'
                    },
                    {
                        'suit': 'Hearts',
                        'value': 'King'
                    }
                ],
                "handValue": 17,
                "isBust": False,
            },
            "player": {
                "hand": [
                    {
                        'suit': 'Spades',
                        'value': '7'
                    },
                    {
                        'suit': 'Hearts',
                        'value': 'King'
                    },
                    {
                        'suit': 'Clubs',
                        'value': 'Ace'
                    }
                ],
                "handValue": 18,
                "isBust": False
            },
            "winner": "Player"
        }


def test_start_blackjack_game_player_bust():
    with patch('app.GameDeck.game_deck.GameDeck') as MockGameDeck:
        mock_game_deck = Mock()
        mock_game_deck.deal_cards.return_value = pydealer.Stack(cards=[test_card_7, test_card_king])
        mock_game_deck.hit.return_value = pydealer.Stack(cards=[test_card_7])
        MockGameDeck.return_value = mock_game_deck

        test_blackjack_game = play_blackjack.PlayBlackJack()
        assert test_blackjack_game.get_game_status() == {
            "playerTurn": True,
            "dealer": {
                "hand": [
                    {
                        'suit': 'Spades',
                        'value': '7'
                    }
                ],
                "handValue": 7,
                "isBust": False,
            },
            "player": {
                "hand": [
                    {
                        'suit': 'Spades',
                        'value': '7'
                    },
                    {
                        'suit': 'Hearts',
                        'value': 'King'
                    }
                ],
                "handValue": 17,
                "isBust": False
            },
            "winner": None
        }

        assert test_blackjack_game.player_hit() == {
            "playerTurn": False,
            "dealer": {
                "hand": [
                    {
                        'suit': 'Spades',
                        'value': '7'
                    },
                    {
                        'suit': 'Hearts',
                        'value': 'King'
                    }
                ],
                "handValue": 17,
                "isBust": False,
            },
            "player": {
                "hand": [
                    {
                        'suit': 'Spades',
                        'value': '7'
                    },
                    {
                        'suit': 'Hearts',
                        'value': 'King'
                    },
                    {
                        'suit': 'Spades',
                        'value': '7'
                    }
                ],
                "handValue": 24,
                "isBust": True
            },
            "winner": "Dealer"
        }


def test_start_blackjack_game_dealer_winner():
    with patch('app.GameDeck.game_deck.GameDeck') as MockGameDeck:
        mock_game_deck = Mock()
        mock_game_deck.deal_cards.return_value = pydealer.Stack(cards=[test_card_5, test_card_king])
        mock_game_deck.hit.return_value = pydealer.Stack(cards=[test_card_5])
        MockGameDeck.return_value = mock_game_deck

        test_blackjack_game = play_blackjack.PlayBlackJack()
        assert test_blackjack_game.get_game_status() == {
            "playerTurn": True,
            "dealer": {
                "hand": [
                    {
                        'suit': 'Spades',
                        'value': '5'
                    }
                ],
                "handValue": 5,
                "isBust": False,
            },
            "player": {
                "hand": [
                    {
                        'suit': 'Spades',
                        'value': '5'
                    },
                    {
                        'suit': 'Hearts',
                        'value': 'King'
                    }
                ],
                "handValue": 15,
                "isBust": False
            },
            "winner": None
        }

        assert test_blackjack_game.play_dealer() == {
            "playerTurn": False,
            "dealer": {
                "hand": [
                    {
                        'suit': 'Spades',
                        'value': '5'
                    },
                    {
                        'suit': 'Hearts',
                        'value': 'King'
                    },
                    {
                        'suit': 'Spades',
                        'value': '5'
                    }
                ],
                "handValue": 20,
                "isBust": False,
            },
            "player": {
                "hand": [
                    {
                        'suit': 'Spades',
                        'value': '5'
                    },
                    {
                        'suit': 'Hearts',
                        'value': 'King'
                    }
                ],
                "handValue": 15,
                "isBust": False
            },
            "winner": "Dealer"
        }


def test_start_blackjack_game_dealer_bust():
    with patch('app.GameDeck.game_deck.GameDeck') as MockGameDeck:
        mock_game_deck = Mock()
        mock_game_deck.deal_cards.return_value = pydealer.Stack(cards=[test_card_5, test_card_king])
        mock_game_deck.hit.return_value = pydealer.Stack(cards=[test_card_king])
        MockGameDeck.return_value = mock_game_deck

        test_blackjack_game = play_blackjack.PlayBlackJack()
        assert test_blackjack_game.get_game_status() == {
            "playerTurn": True,
            "dealer": {
                "hand": [
                    {
                        'suit': 'Spades',
                        'value': '5'
                    }
                ],
                "handValue": 5,
                "isBust": False,
            },
            "player": {
                "hand": [
                    {
                        'suit': 'Spades',
                        'value': '5'
                    },
                    {
                        'suit': 'Hearts',
                        'value': 'King'
                    }
                ],
                "handValue": 15,
                "isBust": False
            },
            "winner": None
        }

        assert test_blackjack_game.play_dealer() == {
            "playerTurn": False,
            "dealer": {
                "hand": [
                    {
                        'suit': 'Spades',
                        'value': '5'
                    },
                    {
                        'suit': 'Hearts',
                        'value': 'King'
                    },
                    {
                        'suit': 'Hearts',
                        'value': 'King'
                    }
                ],
                "handValue": 25,
                "isBust": True,
            },
            "player": {
                "hand": [
                    {
                        'suit': 'Spades',
                        'value': '5'
                    },
                    {
                        'suit': 'Hearts',
                        'value': 'King'
                    }
                ],
                "handValue": 15,
                "isBust": False
            },
            "winner": "Player"
        }


def test_start_blackjack_game_push():
    with patch('app.GameDeck.game_deck.GameDeck') as MockGameDeck:
        mock_game_deck = Mock()
        mock_game_deck.deal_cards.return_value = pydealer.Stack(cards=[test_card_7, test_card_king])
        mock_game_deck.hit.return_value = pydealer.Stack(cards=[test_card_ace])
        MockGameDeck.return_value = mock_game_deck

        test_blackjack_game = play_blackjack.PlayBlackJack()
        assert test_blackjack_game.get_game_status() == {
            "playerTurn": True,
            "dealer": {
                "hand": [
                    {
                        'suit': 'Spades',
                        'value': '7'
                    }
                ],
                "handValue": 7,
                "isBust": False,
            },
            "player": {
                "hand": [
                    {
                        'suit': 'Spades',
                        'value': '7'
                    },
                    {
                        'suit': 'Hearts',
                        'value': 'King'
                    }
                ],
                "handValue": 17,
                "isBust": False
            },
            "winner": None
        }

        assert test_blackjack_game.play_dealer() == {
            "playerTurn": False,
            "dealer": {
                "hand": [
                    {
                        'suit': 'Spades',
                        'value': '7'
                    },
                    {
                        'suit': 'Hearts',
                        'value': 'King'
                    }
                ],
                "handValue": 17,
                "isBust": False,
            },
            "player": {
                "hand": [
                    {
                        'suit': 'Spades',
                        'value': '7'
                    },
                    {
                        'suit': 'Hearts',
                        'value': 'King'
                    }
                ],
                "handValue": 17,
                "isBust": False
            },
            "winner": "Push"
        }
