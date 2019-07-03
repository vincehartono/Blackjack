import random, sys, os

#to suppress all the print()
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

#to deal random cards from the deck
def deal(cards):
    return random.choice(cards)

#to add the first 2 cards dealt (for players & dealers)
def total_cards(x):

    tot = 0
    aces = 0
    for card in x:
        if card in ["J", "Q", "K"]:
            tot += 10
        elif card == "A":
            aces += 1
        else: tot += int(card)

    tot += aces

    while tot + 10 <= 21 and aces > 0:
        tot += 10
        aces -= 1

    return tot

#Dealer first card
def dealer_card(x):

    if x in ["J", "Q", "K"]:
        first = 10
    elif x == "A":
        first = 11
    else: first = int(x)

    return first

#Checking blackjack

#Offering insurance

#Double

#Splitting

#indicator for dealers to hit according to the table's rules
def dealer_min(dealer_total):
    return True if dealer_total < 17 else False

#THE GAME

def play_game(n, amount):

    win = 0
    loss = 0

    for i in range(n):
        #PLAYERS TURN
        player_hand = [deal(cards) for i in range(2)]

        print("PLAYER'S TURN:")
        print("First card is : %s" %player_hand[0])
        print("Second card is : %s" %player_hand[1])

        player_total = total_cards(player_hand)

        print("Player total card is : %d" %player_total)

        #DEALERS showing first card
        dealer_hand = [deal(cards) for i in range(2)]

        print("")
        print("DEALER'S TURN:")
        print("First card is : %s" %dealer_hand[0])

        dealer_first = dealer_card(dealer_hand[0])

        #Players hit if total less than 12 or if between 12 - 17 and dealer showing 7 or greater
        while player_total < 12 or player_total < 17 and dealer_first > 6:
            print("")
            print("PLAYER'S TURN:")
            player_hand.append(deal(cards))
            print("Player next card is : %s" %player_hand[-1])
            player_total = total_cards(player_hand)
            print("Player total card is : %d" % player_total)

        #Player busted
        if player_total > 21:
            print("Player busted!")
            loss += 1
            continue

        #Dealer turn if player is not busted
        print("")
        print("DEALER'S TURN:")
        print("First card is : %s" %dealer_hand[0])
        print("Second card is : %s" %dealer_hand[1])
        dealer_total = total_cards(dealer_hand)
        print("Dealer total card is : %d" %dealer_total)

        while dealer_total < 17:
            dealer_hand.append(deal(cards))
            print("Dealer next card is : %s" % dealer_hand[-1])
            dealer_total = total_cards(dealer_hand)
            print("Dealer total card is : %d" % dealer_total)

        if dealer_total > 21:
            print("Dealer busted!")
            print("Player won!")
            win += 1
            continue

        print("")

        if player_total > dealer_total:
            print ("Player won!")
            win += 1
        elif player_total == dealer_total:
            print ("Tie game")
        else:
            print ("Player lost!")
            loss += 1

        print("-" * 60)

    score = amount + win - loss

    return [score, win, loss]

cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

amount = int(input("How much do you want to change? "))
no_games = int(input("How many games? "))

blockPrint()
balance = play_game(no_games, amount)

enablePrint()
print("Starting money = %d" %amount)
print("Balance = %d" %balance[0])
print("Total Win = %d" %balance[1])
print("Total Loss = %d" %balance[2])
