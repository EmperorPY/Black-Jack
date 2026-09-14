import random

print("Welcome to Blackjack.\n")

cards = {
    "Ace": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10
}

dealer_cards = []
player_cards = []

wins = 0
losses = 0
ties = 0


def deal():
    global wins, losses, ties
    while True:
        dealer_cards.append(random.choice(list(cards.values())))

        if sum(dealer_cards) > 21 and 11 in dealer_cards:
            dealer_cards[dealer_cards.index(11)] = 1


        if sum(dealer_cards) > 21:
            print("Dealer busts!")
            wins += 1
            play_again()

        elif sum(dealer_cards) == 21:
            print("Dealer has 21!")
            losses += 1
            play_again()
            

        elif sum(dealer_cards) > 16:
            print("Dealer has", sum(dealer_cards))
            break
            
            


def player_turn():
    global wins, losses, ties

    while True:
        player_choice_1 = input(
            "Do you want to (h)it or (s)tand? "
        ).strip().lower()

        if player_choice_1 == "h":
            player_cards.append(random.choice(list(cards.values())))

            if sum(player_cards) > 21 and 11 in player_cards:
                player_cards[player_cards.index(11)] = 1

            print("You have", sum(player_cards))

            if sum(player_cards) > 21:
                print("You bust!\n")
                losses += 1
                play_again()

            elif sum(player_cards) < 21:
                continue
            if sum(player_cards) == 21:
                print("Black Jack! You win!")
                wins += 1
                play_again()

        elif player_choice_1 == "s":
            if sum(player_cards) > sum(dealer_cards):
                print("You win!\n")
                wins += 1
                play_again()

            elif sum(player_cards) < sum(dealer_cards):
                print("You lose!\n")
                losses += 1
                play_again()

            else:
                print("It's a tie!\n")
                ties += 1
                play_again()


def play_again():
    global wins, losses, ties
    print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}\n")

    play_again = input(
        "Do you want to play again? (y/n) "
    ).lower().strip()

    if play_again == "y":
        main()
    else:
        print("Bye!")
        exit()


def main():
    global wins, losses, ties
    dealer_cards.clear()
    player_cards.clear()

    deal()
    player_turn()
    main()


main()
