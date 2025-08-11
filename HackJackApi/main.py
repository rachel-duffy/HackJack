from app.PlayBlackJack import play_blackjack


def main():
    print("\nWelcome to HackJack CLI! Game is starting, good luck!")
    print("*******************************************************\n\n")
    blackjack_game = play_blackjack.PlayBlackJack()
    blackjack_game.play()


if __name__ == "__main__":
    main()