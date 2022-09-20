from random import shuffle
# Beginning with one basic deck of cards, a list is created.
card_values = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "King", "Queen", "Joker"]

# A traditional deck has 4 sets of cards, with one card value per each suit
card_deck = []
for card_value in card_values:
    card_deck.extend([card_value, card_value, card_value, card_value])

# This function creates the initial hand for each player.


def create_hands():
    dealer_hand = []
    player_hand = []
    shuffle(card_deck)
    for i in range(2):
        card = card_deck.pop()
        dealer_hand.append(card)
    for i in range(2):
        card = card_deck.pop()
        player_hand.append(card)
    return dealer_hand, player_hand

# These two functions take the dealer's hand and the player's hand, and sums up each card for the total hand.


def sum_player_hand(player_hand):
    player_total = 0
    for card_value in player_hand:
        if card_value == "King":
            player_total += 10
        elif card_value == "Queen":
            player_total += 10
        elif card_value == "Joker":
            player_total += 10
        elif card_value == "Ace":
            if player_total >= 11:
                player_total += 1
            else:
                player_total += 11
        else:
            player_total += card_value
    return player_total


def sum_dealer_hand(dealer_hand):
    dealer_total = 0
    for card_value in dealer_hand:
        if card_value == "King":
            dealer_total += 10
        elif card_value == "Queen":
            dealer_total += 10
        elif card_value == "Joker":
            dealer_total += 10
        elif card_value == "Ace":
            if dealer_total >= 11:
                dealer_total += 1
            else:
                dealer_total += 11
        else:
            dealer_total += card_value
    return dealer_total


# This function checks to see if either dealer or player has a blackjack, and returns true if one of the players do.


def check_blackjack(dealer_total, player_total):
    dealer_has_blackjack = False
    player_has_blackjack = False
    if dealer_total == 21 and player_total != 21:
        dealer_has_blackjack = True
    elif dealer_total != 21 and player_total == 21:
        player_has_blackjack = True
    elif dealer_total == 21 and player_total == 21:
        dealer_has_blackjack = False
        player_has_blackjack = False
    else:
        dealer_has_blackjack = False
        player_has_blackjack = False
    return dealer_has_blackjack, player_has_blackjack


# This function checks the player's and dealer's total and determines the winner.


def check_hand(dealer_total, player_total):
    if dealer_total == 21 and player_total == 21:
        print("You both have a Blackjack. You break even. \n")
    elif dealer_total > 21:
        print("Dealer's hand is higher than 21, dealer busts. You win. \n")
    elif player_total > 21:
        print("Player's hand is higher than 21, player busts. Dealer wins. \n")
    elif player_total > dealer_total:
        print("Player has a higher hand than the Dealer. Player wins.\n")
    elif dealer_total > player_total:
        print("Dealer has a higher hand than the Player. Dealer wins.\n")
    elif dealer_total == player_total:
        print("You both have the same hand. You break even. \n")

# This function restarts blackjack() after a round has ended.


def restart():
    restart = int(input("Press 1 to play again, or 2 to quit the program. \n"))
    global card_values
    if restart == 1:
        shuffle(card_deck)
        print("---------------------------------------------------------------------------------------------------- \n")
        blackjack()
    elif restart == 2:
        print("Thanks for playing! \n")
        quit()


# This function starts the blackjack game.


def blackjack():
    global card_values
    global card_deck
    print("Welcome to the casino. Please step up for a game of blackjack. \n")
    dealer_hand, player_hand = create_hands()
    dealer_total = sum_dealer_hand(dealer_hand)
    player_total = sum_player_hand(player_hand)
    dealer_has_blackjack, player_has_blackjack = check_blackjack(dealer_total, player_total)
    print("Your hand is " + str(player_hand) + ". \n")
    print("Your total is " + str(player_total) + ". \n")
    print("The dealer's first card is " + str(dealer_hand[0]) + ". \n")
    if dealer_has_blackjack is True and player_has_blackjack is False:
        print("The Dealer has a Blackjack. Dealer wins. \n")
        restart()
    elif dealer_has_blackjack is False and player_has_blackjack is True:
        print("The Player has a Blackjack. You win. \n")
        restart()
    else:
        while player_total < 21:
            choice = int(input("Press 1 if you would like to hit, or press 2 if you would like to stand. \n"))
            while dealer_total < 17:
                card = card_deck.pop()
                dealer_hand.append(card)
                dealer_total = sum_dealer_hand(dealer_hand)
                if dealer_total > 21:
                    print("The dealer total is " + str(dealer_total) + ". \n")
                    check_hand(dealer_total, player_total)
                    restart()
            if choice == 1 and dealer_total <= 21:
                card = card_deck.pop()
                player_hand.append(card)
                player_total = sum_player_hand(player_hand)
                print("Your new total is " + str(player_total) + ". \n")
            if choice == 2:
                break
        print("The dealer total is " + str(dealer_total) + ". \n")
        check_hand(dealer_total, player_total)
        restart()


blackjack()
